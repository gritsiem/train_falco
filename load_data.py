from roboflow import Roboflow
from dotenv import load_dotenv
import os

load_dotenv()

rf = Roboflow(api_key=os.getenv('heridal_key'))

project = rf.workspace("new-workspace-qsuag").project("heridal-t428z")
version = project.version(2)
dataset = version.download("yolov8")

if 