from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('yolo11l.pt')
    results = model.train(data='dataset/data.yaml', epochs=20)