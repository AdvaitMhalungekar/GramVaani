from transformers import AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch
import requests

# Load image
image = Image.open("C:/Users/advai/OneDrive/Desktop/download3.jpg")  # or use Image.open(BytesIO(...)) for stream

# Load processor & model
processor = AutoImageProcessor.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")
model = AutoModelForImageClassification.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Preprocess the image
inputs = processor(images=image, return_tensors="pt").to(device)

# Inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax(-1).item()

# Get label
label = model.config.id2label[predicted_class]
print("Predicted disease:", label)
