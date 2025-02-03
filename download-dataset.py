from roboflow import Roboflow
import os

rf = Roboflow(api_key=os.getenv("ROBOFLOW_API_KEY"))
project = rf.workspace("ashspace-7icj2").project("lethal-yolo")
version = project.version(1)
dataset = version.download("yolov11")
