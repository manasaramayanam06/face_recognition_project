import face_recognition
import cv2
import numpy as np
import os
import csv
from datetime import datetime
import time

# Load known faces
known_face_encodings = []
known_face_names = []

folder_path = 'known_faces'  # Ensure this folder exists with known faces

print("🔍 Loading known faces...")
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(folder_path, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_face_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_face_names.append(name)
            print(f"✅ Loaded encoding for {name}")
        else:
            print(f"❌ No face found in {filename}")
    else:
        print(f"📁 Skipped unsupported file: {filename}")

if not known_face_encodings:
    print("⚠ No known face encodings found. Exiting.")
    exit()

# Track already marked names
marked_names = set()

# ==========================
# Daily Attendance File
# ==========================
today_date = datetime.now().strftime("%Y-%m-%d")
csv_filename = f"attendance_{today_date}.csv"

file_exists = os.path.isfile(csv_filename)

attendance_file = open(csv_filename, 'a', newline='', encoding='utf-8')
writer = csv.writer(attendance_file)

# Write header if file is new
if not file_exists or os.stat(csv_filename).st_size == 0:
    writer.writerow(['Name', 'Date', 'Time', 'Status'])

# Start webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("🚫 Could not open webcam.")
    exit()

print("🎥 Webcam started. Press 'Q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("⚠ Failed to grab frame.")
        break

    # Resize and convert frame to RGB
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop over faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare faces
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if face_distances[best_match_index] < 0.45:  # Strict match threshold
            name = known_face_names[best_match_index]

        # Scale back face location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw bounding box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 10),
                    cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255), 2)

        # Mark attendance
        if name != "Unknown" and name not in marked_names:
            date_now = datetime.now().strftime('%Y-%m-%d')
            time_now = datetime.now().strftime('%H:%M:%S')
            writer.writerow([name, date_now, time_now, 'Present'])
            attendance_file.flush()
            os.fsync(attendance_file.fileno())
            marked_names.add(name)

            print(f"📝 Marked attendance for {name} at {date_now} {time_now}")
            print(f"📂 Saved to: {os.path.abspath(csv_filename)}")

            # Display message
            cv2.putText(frame, "Attendance Marked", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)
            cv2.imshow('Face Recognition Attendance', frame)
            cv2.waitKey(2000)  # Wait 2 seconds
            break  # Move to next person

    # Show live webcam feed
    cv2.imshow('Face Recognition Attendance', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
attendance_file.close()
cv2.destroyAllWindows()
print("👋 Program ended.")
