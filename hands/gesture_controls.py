import numpy as np
import cv2
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key, Listener
import time

class GestureControls:
    def __init__(self):
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        
        self.cursor_mode = False  # Default to Volume Mode

        # --- Volume Control (Thumb Up/Down) ---
        self.volume_threshold_up = 0.15  # Thumb above wrist → Volume Up
        self.volume_threshold_down = 0.15  # Thumb below wrist → Volume Down

        # --- Cursor Movement ---
        self.screen_width, self.screen_height = 1920, 1080
        self.default_dpi = 1.0  
        
        # --- Click/Drag Detection ---
        self.click_threshold = 0.1  
        self.release_threshold = self.click_threshold * 1.5  
        self.left_click_held = False

        # Smoothing parameters for cursor movement:
        self.smoothing_alpha = 0.2
        self.smoothed_position = None

        # Start keyboard listener for mode switching:
        self.listener = Listener(on_press=self.on_key_press)
        self.listener.start()

    def on_key_press(self, key):
        """Handles keyboard input for mode switching."""
        try:
            if key.char == 'c':  # Toggle to Cursor Mode
                self.cursor_mode = True
                print("Cursor Mode Activated")
            elif key.char == 'v':  # Toggle to Volume Mode
                self.cursor_mode = False
                print("Switched to Volume Mode")
        except AttributeError:
            pass  # For special keys

    def control_volume(self, hand_landmarks, frame):
        """Controls volume based on thumb position relative to wrist."""
        if self.cursor_mode:
            return frame

        landmarks = hand_landmarks.landmark
        thumb_tip = landmarks[4]
        wrist = landmarks[0]

        if thumb_tip.y < wrist.y - self.volume_threshold_up:
            self.keyboard.press(Key.media_volume_up)
            self.keyboard.release(Key.media_volume_up)
            print("Volume Up (Thumb Up)")
        elif thumb_tip.y > wrist.y + self.volume_threshold_down:
            self.keyboard.press(Key.media_volume_down)
            self.keyboard.release(Key.media_volume_down)
            print("Volume Down (Thumb Down)")

        return frame

    def move_cursor(self, hand_landmarks):
        """Moves the mouse cursor using a smoothed position to reduce jitter."""
        landmarks = hand_landmarks.landmark
        index_tip = landmarks[8]

        # Calculate new screen coordinates from normalized position:
        new_x = index_tip.x * self.screen_width * self.default_dpi
        new_y = index_tip.y * self.screen_height * self.default_dpi
        if self.smoothed_position is None:
            self.smoothed_position = (new_x, new_y)
        else:
            smoothed_x = self.smoothed_position[0] * (1 - self.smoothing_alpha) + new_x * self.smoothing_alpha
            smoothed_y = self.smoothed_position[1] * (1 - self.smoothing_alpha) + new_y * self.smoothing_alpha
            self.smoothed_position = (smoothed_x, smoothed_y)
        self.mouse.position = (int(self.smoothed_position[0]), int(self.smoothed_position[1]))
        print(f"Cursor Position: ({int(self.smoothed_position[0])}, {int(self.smoothed_position[1])})")

    def draw_ui(self, frame, hand_landmarks):
        """Draws the mode text and hand landmarks on the camera feed."""
        h, w, _ = frame.shape

        mode_text = "Cursor Mode" if self.cursor_mode else "Volume Mode"
        mode_color = (255, 0, 0) if self.cursor_mode else (0, 255, 0)
        cv2.putText(frame, mode_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, mode_color, 2)

        for lm in hand_landmarks.landmark:
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        return frame
