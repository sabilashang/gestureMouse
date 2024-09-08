import cv2
import mediapipe as mp
import pyautogui

# Initialize hand detector and drawing utils
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)   # Capture video from the webcam

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    frame_height = frame_height
    frame_width = frame_width
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            #index_x = index_y = thumb_x = thumb_y = middle_x = middle_y = 0
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:  # Index finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y, duration=0.05)
                elif id == 4:  # Thumb tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                elif id == 12:  # Middle finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y

            # Detect left click (index and thumb close together)
            if abs(index_y - thumb_y) < 45:
                pyautogui.leftClick()
                pyautogui.sleep(0.15)

            # Detect right click (thumb and middle finger close together)
            if abs(middle_y - thumb_y) < 45:
                pyautogui.rightClick()
                pyautogui.sleep(0.15)

    cv2.imshow('vMouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()