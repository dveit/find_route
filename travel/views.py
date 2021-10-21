from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name = 'Dmitry'
    return render(request, 'home.html', {'name': name})

def about(request):
    text = 'About us'
    return render(request, 'about.html', {'text': text})
