from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def sample(self):
    return HttpResponse('hello')

def home(request):
    return render(request,'home.html')