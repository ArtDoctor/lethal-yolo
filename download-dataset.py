from roboflow import Roboflow

rf = Roboflow(api_key="V8hkEWY7apLYPHW6Mk7F")
project = rf.workspace("ashspace-7icj2").project("lethal-company-object-detection-v2")
version = project.version(2)
dataset = version.download("yolov11")
