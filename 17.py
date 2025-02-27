import cv2
import numpy as np
from ultralytics import YOLO


model = YOLO("yolov8n.pt")

base_image = cv2.imread("input.jpg")

overlay_image = cv2.imread("overlay.png", cv2.IMREAD_UNCHANGED)

results = model(base_image)

for result in results:
    for box in result.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)

        resized_overlay = cv2.resize(overlay_image, (x2 - x1, y2 - y1))

        base_image[y1:y2, x1:x2] = resized_overlay[:, :, :3]

cv2.imwrite("output.jpg", base_image)

cv2.imshow("Result", base_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
