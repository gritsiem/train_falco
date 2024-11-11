
# from ultralytics import YOLO
import os
import random

# model = YOLO("yolov8l.pt")
# model.info()
random.seed(0)
slurmscratch = os.environ.get("SLURM_SCRATCH")
print("slurm is data path: ", slurmscratch)
datadir=os.path.join(slurmscratch,"Heridal-2")
train = os.path.join(datadir,"train","images")
trlabels = os.path.join(datadir,"train","labels")
labelfiles = os.listdir(trlabels)
valid = os.path.join(datadir,"valid")
#os.mkdir(os.path.join(valid,"images"))
#os.mkdir(os.path.join(valid,"labels"))

print("Now creating val set")
fns = random.choices(os.listdir(train),k = 150)
#l = len(os.listdir(os.path.join(valid,"labels")))
print(len(fns))

for fn in fns:
    num = fn[6:14]
    labelfile = [ lf for lf in labelfiles if num in lf][0]
    os.replace(os.path.join(train,fn),os.path.join(valid, "images",fn))
    os.replace(os.path.join(trlabels,labelfile),os.path.join(valid, "labels",labelfile))
    #try:
    #    os.replace(os.path.join(train,fn),os.path.join(valid, "images",fn))
    #    os.replace(os.path.join(train,labelfile),os.path.join(valid, "labels",fn))
    #except FileNotFoundError:
    #    continue
l = len(os.listdir(os.path.join(valid,"labels")))
print(l,"files created")
