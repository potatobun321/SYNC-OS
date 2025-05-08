this project is an actual real-time hand gesture-based computer system designed with Python, OpenCV, MediaPipe, and the pynput library. 
The users can now manipulate their mouse pointer and computer system volume by performing natural finger actions without needing to touch the hardware.
The index finger is responsible for controlling the cursor location on the screen, mimicking mouse movement in real time. There is also volume control mode that employs distance between fingers to raise or lower system volume. 
The system incorporates gesture hysteresis to prevent jittery motion and provides a smooth user experience.(EARLY DEVELOPMENT PHASE)
It is modular in design, with the hand tracking logic (hand_tracking_module.py) and gesture control logic (gesture_controls.py) being decoupled from the main application (main.py). 
The project is executed within a virtual environment (gesture_env) to ensure dependency isolation, and a.gitignore file is employed to ignore unnecessary files such as the virtual environment from version control. 
This simple and light tool is a gesture-based desktop environment prototype and illustrates the potential for computer vision to be used to develop touchless, gesture-based interfaces.

---
SETUP INSTRUCTIONS 
# Clone the repository
git clone https://github.com/potatobun321/SYNC-OS.git

---

cd hands

# Activate virtual environment (replace with your actual env path if needed)
source ~/gesture_env/bin/activate

# Install dependencies
pip install opencv-python mediapipe pynput
