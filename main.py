from PIL import Image
import cv2
from util import get_limits
cap = cv2.VideoCapture(0)

yellow = [0, 255, 255] # BGR colorspace
red = [0, 0, 255]       # Red color in BGR
blue = [255, 0, 0]      # Blue color in BGR
green = [0, 255, 0]     # Green color in BGR
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Yellow color detection
    yellow_lower, yellow_upper = get_limits(color=yellow)
    yellow_mask = cv2.inRange(hsvImage, yellow_lower, yellow_upper)

    bbox = Image.fromarray(yellow_mask).getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1, y1), (x2, y2), yellow, 5)
        cv2.putText(frame, "Yellow", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, yellow, 2)

    # Red color detection
    red_lower, red_upper = get_limits(color=red)
    red_mask = cv2.inRange(hsvImage, red_lower, red_upper)

    bbox = Image.fromarray(red_mask).getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1, y1), (x2, y2), [0, 0, 255], 5)
        cv2.putText(frame, "Red", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [0, 0, 255], 2)

    # Blue color detection
    blue_lower, blue_upper = get_limits(color=blue)
    blue_mask = cv2.inRange(hsvImage, blue_lower, blue_upper)

    bbox = Image.fromarray(blue_mask).getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1, y1), (x2, y2), blue, 5)
        cv2.putText(frame, "Blue", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, blue, 2)

    # Green color detection
    green_lower, green_upper = get_limits(color=green)
    green_mask = cv2.inRange(hsvImage, green_lower, green_upper)

    bbox = Image.fromarray(green_mask).getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.putText(frame, "Green", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()