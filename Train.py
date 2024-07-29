#Step 1: Install the Libraries 
#You can directly try this code in jupiter notebook 
#If using Vs code  run the pip commands in ter,kinal then proceed
pip install ultralytics
pip install torch

#Step 2: Import Packages
import torch
from ultralytics import YOLO
 #Step 3: Define the function for the Training the model with required attributes and specifications
def train_model():
    # Load a pre-trained YOLOv8 model
    model = YOLO('yolov8s-seg.pt')  # Using YOLOv8s for a balance between speed and accuracy
 
    # Path to your custom dataset
    #the data.yaml file consists of the info about the annotated dataset
    data_path = "data.yaml"
 
    # Train the model with custom data
    model.train(data=data_path,
                epochs=50,  # Increase epochs if necessary
                batch=16,  # Adjust based on your GPU memory
                imgsz=640,  # Increase image size for better accuracy
                augment=True,  # Enable data augmentation
                patience=5,  # Early stopping if no improvement
                cache=True,  # Cache images for faster training
                device='0',  # GPU device ID
                lr0=0.001,  # Initial learning rate
                optimizer='SGD',  # Optimizer
                weight_decay=0.0005,  # Regularization
                project='custom_yolov8_project',  # Project name
                name='exp',  # Experiment name
                verbose=True)
 
    # Validate the model
    results = model.val()
 
    # Save the trained model
    model.save("  Change this with The DIRECTORY TO SAVE YOUR MODEL   ")
 # After the complete training of the weights are stored in the best.pt file
if __name__ == '__main__':
    train_model()
