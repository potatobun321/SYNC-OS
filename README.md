
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

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/potatobun321/SYNC-OS.git
```

### 2. Navigate to the Project Directory

```bash
cd hands
```

### 3. Activate the Virtual Environment

```bash
source ~/gesture_env/bin/activate
```

### 4. Install Dependencies

```bash
pip install opencv-python mediapipe pynput
```

---

## Current Status

This project is in an **early development phase**. While core gesture functionality is operational, further refinement is planned to improve robustness, gesture recognition accuracy, and overall usability.

---

## Future Scope

* Additional gesture mappings (clicks, scrolling, application control)
* Multi-hand interaction
* Improved smoothing and filtering
* Cross-platform enhancements

---

### PS

*This README file was written and edited with the assistance of ChatGPT.*

---

