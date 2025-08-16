Face Recognition Attendance System:
This project is an AI-powered Attendance System built using Python, OpenCV, and the Face Recognition library.
It detects faces in real-time through a webcam and automatically marks Name, Date, and Time in an Excel file.
Features :
 Real-Time Face Detection using OpenCV
 Recognizes known faces stored in the known_faces/ folder
 Automatically records Name, Date, and Time in attendance.xlsx
 Attendance records are saved for future reference
 Fast and efficient recognition using the face_recognition library
 Tech Stack:
Python 
OpenCV  (for real-time image processing)
Face Recognition  (for identifying faces)
Numpy & Pandas  (for data handling)
Excel (openpyxl)  (for attendance storage)
📂 Project Structure:
face_recognition_project/
│── main.py             # Main script for face recognition & attendance
│── requirements.txt    # List of dependencies
│── known_faces/        # Folder containing images of known people
│── attendance.xlsx     # Excel file to store attendance
│── README.md           # Project documentation
Installation:
git clone https://github.com/your-username/face-recognition-attendance.git
cd face-recognition-attendance
pip install -r requirements.txt
Usage:
Place images of known people in the known_faces/ folder.
Example: known_faces/John.jpg
Run the project:
python main.py
The camera will start and recognize faces in real-time.
Attendance will be stored in attendance.xlsx.
Example Output:
Face detected and recognized via webcam
Attendance automatically marked in Excel
<img width="1355" height="735" alt="Screenshot 2025-08-16 163008" src="https://github.com/user-attachments/assets/31cbdfbc-7edc-4fde-882c-bcf5c1062410" />
<img width="573" height="547" alt="Screenshot 2025-08-16 164640" src="https://github.com/user-attachments/assets/55a5c733-aad9-490c-b4eb-5c4cc3f0367c" />
Contributing:
Pull requests are welcome! If you’d like to improve this project, fork the repo and create a PR.
Contact:
Created by Your manasaramayanam06
