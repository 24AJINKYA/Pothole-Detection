pip install ultralytics
from ultralytics import YOLO
# Load a trained YOLOv8 model
model = YOLO('best.pt')  # Give path Your best.pt
# Path to your custom dataset
#the data.yaml file consists of the info about the annotated dataset
data_path = "data.yaml"
# Train the model with custom data
result=model.val()
print(result)
# From the Results You can See many graphs and charts including the Confusion Matrix .
# Using this data the accuracy precision , Recall , F1 score , etc insights can be calculated .
# If the testing accuracy is to be calculated , then in data.yaml just change the path of the 'val:' and give there oath to test/images.
