from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import predict_image


# 🔹 Landing Page
def landing(request):
    return render(request, 'landing.html')


# 🔹 Main AI Page
def index(request):

    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)

        prediction = predict_image(fs.path(filename))

        return render(request, 'index.html', {
            'prediction': prediction,
            'image_url': image_url
        })

    return render(request, 'index.html')