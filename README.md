
# SYNC-OS

*A Real-Time Hand Gesture–Based Computer Control System*

SYNC-OS is a real-time, gesture-based desktop interaction prototype built using **Python**, **OpenCV**, **MediaPipe**, and **pynput**. It enables users to control core system functions—such as mouse movement and system volume—using natural hand and finger gestures, without physically touching any hardware.

This project demonstrates the potential of computer vision in creating intuitive, touchless human–computer interfaces.

---

##  Features

* **Real-Time Hand Tracking**
  Uses MediaPipe to detect and track hand landmarks accurately in real time.

* **Mouse Cursor Control**
  The **index finger** controls the mouse pointer position, closely mimicking natural mouse movement.

* **Volume Control Mode**
  Adjust system volume dynamically based on the **distance between fingers**.

* **Gesture Hysteresis**
  Implements hysteresis logic to reduce jitter and provide smoother, more stable interactions *(early development phase)*.

* **Modular Architecture**
  Clean separation of concerns:

  * `hand_tracking_module.py` – hand detection and landmark processing
  * `gesture_controls.py` – gesture interpretation and system control
  * `main.py` – application entry point

* **Lightweight & Extensible**
  Designed as a simple prototype that can be extended into a full gesture-based desktop environment.

---

##  Project Structure

```
hands/
│
├── hand_tracking_module.py
├── gesture_controls.py
├── main.py
├── .gitignore
└── README.md
```

* The project runs inside a **Python virtual environment (`gesture_env`)** to ensure dependency isolation.
* The `.gitignore` file excludes unnecessary files such as the virtual environment directory from version control.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/potatobun321/SYNC-OS.git
cd SYNC-OS
```

---

### 2. Create a Python Virtual Environment

It is recommended to use a virtual environment to isolate project dependencies.

```bash
python3 -m venv gesture_env
```

---

### 3. Activate the Virtual Environment

**Linux / macOS**

```bash
source gesture_env/bin/activate
```

**Windows**

```bash
gesture_env\Scripts\activate
```

If successful, your terminal should now show something like:

```
(gesture_env) user@pc:~/SYNC-OS$
```

---

### 4. Navigate to the Project Folder

```bash
cd hands
```

---

### 5. Install Dependencies

Install the required Python libraries:

```bash
pip install opencv-python mediapipe pynput
```

If you encounter compatibility issues with MediaPipe, install a stable version:

```bash
pip install mediapipe==0.10.21
```

---

### 6. Run the Program

```bash
python main.py
```

Your webcam should open and begin tracking your hand gestures.

---

# Requirements

* Python **3.8 – 3.11**
* Webcam
* Git

---

# Troubleshooting

### MediaPipe Error

If you see:

```
AttributeError: module 'mediapipe' has no attribute 'solutions'
```

Reinstall MediaPipe:

```bash
pip uninstall mediapipe
pip install mediapipe==0.10.21
```

---

### Webcam Not Detected (Linux)

Check if your system detects the camera:

```bash
v4l2-ctl --list-devices
```

If needed, install camera utilities:

```bash
sudo apt install v4l-utils
```

---

# Project Status

SYNC-OS is currently in **early development**.

Current features include:

* Hand tracking
* Cursor control using finger movement
* Basic gesture recognition

## Current Status

This project is in an **early development phase**. While core gesture functionality is operational, further refinement is planned to improve robustness, gesture recognition accuracy, and overall usability.

---

### PS

*This README file was written and edited with the assistance of ChatGPT.*

---

