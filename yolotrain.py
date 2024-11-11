from ultralytics import YOLO
import os

slurmscratch = os.environ.get("SLURM_SCRATCH")
datadir=os.path.join(slurmscratch,"Heridal-2")

model = YOLO("yolov10l.pt")
model.info()

nc = os.cpu_count()
results = model.train(data=os.path.join(datadir,"data.yaml"), epochs=1, batch=1, imgsz=640, device="cpu", workers=nc)