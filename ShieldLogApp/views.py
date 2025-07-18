from django.shortcuts import render

def index(request):
    return render(request,'index.htm')

def homepage(request):
    return render(request, 'homepage.htm')