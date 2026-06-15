from ultralytics import YOLO

model = YOLO("runs/detect/industrial_detection/yolo11m_1280_150epochs/weights/best.pt")

metrics = model.val()

print(f"Precision: {metrics.box.mp:.4f}")
print(f"Recall: {metrics.box.mr:.4f}")
print(f"mAP@50: {metrics.box.map50:.4f}")
print(f"mAP@50-95: {metrics.box.map:.4f}")
