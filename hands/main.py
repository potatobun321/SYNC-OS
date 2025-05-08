from hand_tracking_module import HandTracking
from gesture_controls import GestureControls
from pynput.mouse import Button
import cv2
import time
import math

hand_tracker = HandTracking()
gesture_controller = GestureControls()

cap = cv2.VideoCapture(0)

# Smoothing is handled in gesture_controls.move_cursor()

# Gesture thresholds (using hysteresis)
# Left Click (Index & Thumb)
left_click_trigger_threshold = 0.05    # When index & thumb are closer than this, perform left click
left_click_release_threshold = 0.1       # Fingers must separate above this to reset left click

# Drag Toggle (Index & Middle)
drag_toggle_trigger_threshold = 0.05   # When index & middle are closer than this, toggle drag mode
drag_toggle_release_threshold = 0.08     # Fingers must separate above this to allow a new toggle

# State flags
left_click_active = False    # For left-click gesture state
drag_toggle_active = False   # For drag toggle gesture state detection
drag_mode = False            # Current drag mode state

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hand_landmarks = hand_tracker.process_frame(frame)

    if hand_landmarks:
        if not gesture_controller.cursor_mode:
            # In Volume Mode, process volume control.
            frame = gesture_controller.control_volume(hand_landmarks, frame)
        else:
            # Process gestures for cursor mode using the first detected hand.
            landmarks = hand_landmarks.landmark
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]
            middle_tip = landmarks[12]

            # Update cursor position (smoothing handled in move_cursor)
            gesture_controller.move_cursor(hand_landmarks)

            # --- Left Click using Index & Thumb ---
            dist_index_thumb = math.hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)
            if dist_index_thumb < left_click_trigger_threshold and not left_click_active:
                gesture_controller.mouse.press(Button.left)
                gesture_controller.mouse.release(Button.left)
                print("Left click performed")
                left_click_active = True
            elif dist_index_thumb > left_click_release_threshold:
                left_click_active = False

            # --- Drag Toggle using Index & Middle ---
            dist_index_middle = math.hypot(index_tip.x - middle_tip.x, index_tip.y - middle_tip.y)
            if dist_index_middle < drag_toggle_trigger_threshold and not drag_toggle_active:
                # Toggle drag mode only once per gesture transition.
                if not drag_mode:
                    gesture_controller.mouse.press(Button.left)
                    drag_mode = True
                    print("Drag mode activated")
                else:
                    gesture_controller.mouse.release(Button.left)
                    drag_mode = False
                    print("Drag mode deactivated")
                drag_toggle_active = True
            elif dist_index_middle > drag_toggle_release_threshold:
                drag_toggle_active = False

            frame = gesture_controller.draw_ui(frame, hand_landmarks)
    else:
        # Optionally, reset flags if no hand is detected.
        pass

    cv2.imshow('Hand Gesture OS Control', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
