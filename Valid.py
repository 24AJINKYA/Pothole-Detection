pip install ultralytics
from ultralytics import YOLO
# Load a trained YOLOv8 model
model = YOLO('best.pt')  # Give path og best.pt
# Path to your custom dataset
#the data.yaml file consists of the info about the annotated dataset
data_path = "data.yaml"
# Train the model with custom data
result=model.val()
print(result)
