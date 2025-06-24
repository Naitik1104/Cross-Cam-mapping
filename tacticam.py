from ultralytics import YOLO
model = YOLO("best.pt")
results = model("tacticam.mp4",save=True)