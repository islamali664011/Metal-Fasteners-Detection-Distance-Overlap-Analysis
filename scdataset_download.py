from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")

project = rf.workspace("cracks-oa7kv").project("industrial-project-front-view")
version = project.version(3)

dataset = version.download("yolov11")

print("Dataset downloaded to:", dataset.location)
