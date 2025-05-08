# ✋ Gesture-Based OS Control System

A Python-driven, modular project that allows you to **operate your computer with hand gestures**. Constructed with OpenCV, MediaPipe, and `pynput`, it provides natural, camera-based input for cursor movement, clicking, dragging, and even volume control — without ever touching your mouse or keyboard.

This is one component of a long-term experimental OS project investigating **gesture-first human-computer interaction**, ultimately hoping to run as a different linux distro.

---

Features

Cursor Mode — Extend your index finger to move the mouse
Left Click — Click your thumb and index finger
Drag Toggle — Touch your middle and index fingers to toggle drag mode (stil needs polishing)
Volume Mode  — Gesture-controlled volume (work in progress)


---

Tech Stack

- Python 3.10+
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- Pynput (mouse control)
- external environment used (gesture_env; source /home/kartikay/Downloads/Python-3.12.0/gesture_env/bin/activate)
- Bare minimum dependencies, easy to extend

---

future plans

Add a popup UI to show current mode (cursor/volume)
Use voice cues to trigger gesture layers
Add a configuration system like NixOS for full control
Export as a Linux DE shell (based on Sway)
More gestures, modular functions, and minimal CPU usage

---
Structure

gesture-os
├── main.py # Core loop handling camera + gestures
├── hand_tracking_module.py # Detects hands and draws landmarks
├── gesture_controls.py # Applies gesture logic to OS controls
└── README.txt
