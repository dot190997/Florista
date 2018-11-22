from django.http import HttpResponse
from .models import Flower
from .forms import flowerform
from django.template import loader
from django.shortcuts import render
from keras.preprocessing.image import image
from .cnn import classifier
import numpy as np


def predict(request):
    ans = ['daisy', 'sunflower', 'rose', 'sunflower', 'tulip']
    need = Flower.objects.last()
    predict_path = "C:\\Users\\DELL\\Desktop\\florista\media\\" + str(need.flower_image)
    test_image = image.load_img(predict_path, target_size=(128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    ans2 = 0
    result = result[0]
    result = result.tolist()
    i=0
    for x in result:
        if x == 1:
            ans2 = ans[i]
        i = i+1
    need.flower_name = ans2
    need.save()
    context = {
        'ans2': ans2,
        'need': need,
    }
    return context

def history(request):
    all_images = Flower.objects.all()
    template = loader.get_template('identify/history.html')
    context = {
        'all_images': all_images,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('identify/home.html')
    return HttpResponse(template.render())


def search(request):
    fil = request.GET['q']
    #template = loader.get_template('identify/history.html')
    images = Flower.objects.filter(flower_name=fil)
    context = {
        'all_images': images,
    }
    return images


def fileupload2(request):
    form = flowerform()
    template = loader.get_template('identify/index.html')
    images = search(request)
    return HttpResponse(template.render({'form': form, 'all_images': images}))


def fileupload(request):
    if request.method == 'POST':
        form = flowerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = predict(request)
            template = loader.get_template('identify/predict.html')
            return HttpResponse(template.render(context, request))

    else:
        form = flowerform()
        return render(request, 'identify/index.html', {'form': form})
