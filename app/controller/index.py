from django.shortcuts import render
from django.shortcuts import HttpResponse

def index (request):
    return render(request, "index.html")

def createHtml(request):
    return render(request, "createHtml.html")