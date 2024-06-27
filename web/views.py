from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    images =[
        {
            'img':'static/img/img_1.jpeg',
            'message':'El mejor postre de chocolate que puedes probar', 
        },
        {
            'img':'static/img/img_2.jpeg',
            'message':'Las mejores recetas de la abuela',
        },
        {
            'img':'static/img/img_3.jpeg',
            'message':'No dejes que te lo cuenten, ven y pruebalo',
        }
    ]
    context = {'images': images}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')
