#Step 1: Install the library
pip install ultralytics
#step 2 : Import Packages
from ultralytics import YOLO

#Step 3 : Load the Model
model = YOLO("best.pt") # Edit this with the Path of the Best.pt file 
# pass the necessary Args.
results = model(source="image.png", save=True, conf=0.2) # give to the path of your test image 

print(results)
# You will be getting the result image Stored in the 'runs folder'
