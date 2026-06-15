from ultralytics import YOLO

model = YOLO("yolo11m.pt")

results = model.train(
    data="PATH_TO_DATASET/data.yaml",
    epochs=150,
    imgsz=1280,
    batch=8,
    device=0,
    project="industrial_detection",
    name="yolo11m_1280_150epochs"
)

print("Training finished!")
