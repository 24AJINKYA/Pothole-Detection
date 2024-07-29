

# Load a pre-trained YOLOv8 model
model = YOLO('yolov8s-seg.pt')  # Using YOLOv8s for a balance between speed and accuracy
# Path to your custom dataset
#the data.yaml file consists of the info about the annotated dataset
data_path = "data.yaml"
# Train the model with custom data
result=model.val()
print(result)
