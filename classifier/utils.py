import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import os
from django.conf import settings

# -----------------------------
# Device
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------------
# Create Model FIRST
# -----------------------------
model = models.resnet18(weights=None)

model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
model.maxpool = nn.Identity()
model.fc = nn.Linear(model.fc.in_features, 10)

model = model.to(device)

# -----------------------------
# Load Trained Weights
# -----------------------------
model_path = os.path.join(settings.BASE_DIR, "resnet18_cifar10model.pth")

checkpoint = torch.load(model_path, map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])

model.eval()

# -----------------------------
# CIFAR Classes
# -----------------------------
classes = ['airplane','automobile','bird','cat',
           'deer','dog','frog','horse','ship','truck']

# -----------------------------
# Image Transform
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((32,32)),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465),
                         (0.2023, 0.1994, 0.2010))
])

# -----------------------------
# Prediction Function
# -----------------------------
def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        _, predicted = output.max(1)

    return classes[predicted.item()]