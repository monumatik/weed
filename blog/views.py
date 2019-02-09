from django.shortcuts import render
from .models import Track
# Create your views here.

def home(request):
	tracks = Track.objects.all()
	return render(request, "blog/home.html", {'tracks':tracks})