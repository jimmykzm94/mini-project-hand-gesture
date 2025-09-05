import cv2

# Use a GStreamer pipeline as input
pipeline = "autovideosrc ! videoconvert ! appsink"
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("❌ Could not open pipeline")
    exit()

print("✅ GStreamer pipeline opened")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("GStreamer Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
