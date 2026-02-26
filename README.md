VisionForge – ResNet-Powered AI Vision Engine

VisionForge is a deep learning-based image classification web application built using ResNet-18 and trained on the CIFAR-10 dataset. The project integrates a PyTorch-trained model with a Django backend and a modern frontend interface.
This application allows users to upload an image and receive real-time classification predictions through a deployed AI system.

________________________________________

Project Overview
This project demonstrates:
•	Deep Learning model training using ResNet-18
•	CIFAR-10 dataset preprocessing and augmentation
•	Model optimization and validation
•	Deployment-ready Django backend
•	Modern frontend interface with structured UI flow

________________________________________

Model Details:
•	Architecture: ResNet-18 (modified for CIFAR-10)
•	Input Size: 32 × 32 × 3
•	Dataset: CIFAR-10
•	Classes: 10
•	Validation Accuracy: ~93.7%
•	Loss Function: CrossEntropyLoss with label smoothing
•	Optimizer: SGD with Momentum
•	Scheduler: Cosine Annealing

________________________________________

Supported Classes
The model recognizes the following CIFAR-10 categories:
•	Airplane
•	Automobile
•	Bird
•	Cat
•	Deer
•	Dog
•	Frog
•	Horse
•	Ship
•	Truck
Note: The model is trained specifically on CIFAR-10. It may not perform reliably on unrelated real-world images outside these categories.

________________________________________

Tech Stack:
•	Python
•	PyTorch
•	Django
•	HTML5
•	CSS3
•	Gunicorn
•	WhiteNoise

________________________________________

Project Structure:
•	cifar10_project/
•	classifier/
•	templates/
•	static/
•	utils.py
•	views.py
•	models.py
•	resnet18_cifar10model.pth
•	manage.py
•	requirements.txt
•	Procfile

________________________________________

Installation (Local Setup):
•	Clone the repository
git clone https://github.com/shivampa859/visionforge-ai.git
•	Navigate to the project folder
cd visionforge-ai
•	Create virtual environment
python -m venv venv
•	Activate environment
Windows:
venv\Scripts\activate
•	Install dependences
pip install -r requirements.txt
•	Run development server
python manage.py runserver
Visit:
http://127.0.0.1:8000/

________________________________________

Deployment:
This project is deployed using Render.
Production setup includes:
•	Gunicorn WSGI server
•	WhiteNoise for static file handling
•	DEBUG set to False
•	Proper static configuration

________________________________________

Key Learning Outcomes
•	Modifying ResNet-18 for small image datasets
•	Preventing overfitting using augmentation and scheduling
•	Integrating PyTorch models into Django
•	Managing static and media files in production
•	Handling cloud deployment for AI applications

________________________________________

Author
Shivam Patel
Deep Learning and Computer Vision Enthusiast

