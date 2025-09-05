import cv2
import mediapipe as mp

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# GStreamer pipeline (UDP H264 input)
pipeline = (
    "udpsrc port=5000 ! "
    "application/x-rtp,encoding-name=H264 ! "
    "rtph264depay ! avdec_h264 ! videoconvert ! appsink"
)

cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

def classify_gesture(landmarks):
    # Example: detect "thumbs up"
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    if thumb_tip.y < index_tip.y:  # thumb higher than index
        return "Thumbs Up"
    return "Open Hand"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Frame not received")
        break

    # Convert BGR to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = ""
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            landmarks = handLms.landmark
            gesture = classify_gesture(landmarks)

    cv2.putText(frame, gesture, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
