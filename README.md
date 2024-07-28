#Pothole Detection using YOLOv8

This repository contains the implementation of an object detection model specifically designed for pothole detection. The model is trained using the YOLOv8s architecture, which is selected for its balance of speed and accuracy.

**Model Overview**
YOLOv8 offers multiple model variants (s, n, l, x), each catering to different use cases based on computational resources and performance needs. For this project, we have employed the YOLOv8s model, which is optimized for faster inference while maintaining good detection accuracy.

**Dataset**
The dataset used for training the model is compiled from various sources:
•	Kaggle: A collection of publicly available images.
•	Locality: Images captured from local areas to add diversity and real-world scenarios to the dataset.

**Training Details**
•	Image Size: 640x640 pixels
•	Epochs: 50
•	Early Stopping: The model training uses the patience parameter set to 5, which means training stops if there is no improvement in the validation metrics for 5 consecutive epochs.
•	Weights Storage: Upon completion of training, the model stores the final weights in the best.pt file located in the weights section.

**Results**
The trained model can accurately detect potholes in various conditions, providing a reliable solution for road safety and maintenance applications.
