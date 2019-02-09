from django.shortcuts import render
from .models import Track
from django.core.paginator import Paginator
# Create your views here.

def home(request):
	tracks = Track.objects.all()
	return render(request, "home.html", {'tracks':tracks})