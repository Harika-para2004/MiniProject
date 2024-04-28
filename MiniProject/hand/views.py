from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . import hand_model
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def test(request):
    
    return render(request,'test.html')
def document(request):
    return render(request,'documentation.html')

def runmodel(request):
    hand_model.hand_gesture()
    return render(request,'runmodel.html')