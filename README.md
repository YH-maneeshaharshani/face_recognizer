# Real-Time Face Recognition System

A Python-based face detection and recognition system built using OpenCV, SQLite, and the Local Binary Patterns Histograms (LBPH) algorithm. The application captures face images from a webcam feed, stores student profiles in a database, trains a machine learning model, and predicts identities in real-time.

---

## 📁 Project Structure

```text
face_recognizer/
│
├── dataset/                           # Stores captured face samples (user.ID.SampleNum.jpg)
├── recognizer/                        # Stores the trained model file
│   └── trainningData.yml              # Trained LBPH face recognizer weights
├── database.db                        # SQLite database holding student details
├── haarcascade_frontalface_default.xml # Haar Cascade XML file for face detection
│
├── dataset_creater.py                 # Script 1: Database entry & dataset generation
├── trainer.py                         # Script 2: Model training on saved dataset
└── detect.py                          # Script 3: Real-time face detection & profile display
