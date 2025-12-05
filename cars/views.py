from django.http import HttpResponse
from django.shortcuts import render

from .models import Car, CarCategory

def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, "index.html", context)

def cars_page(request):
    categories = CarCategory.objects.all()
    context = {'categories': categories}
    return render(request, "cars.html", context)

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact_us(request):
    return HttpResponse("Страница для связи с нами")

