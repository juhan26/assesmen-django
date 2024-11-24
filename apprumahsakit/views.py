from django.shortcuts import render
from .models import Kamar

# Create your views here.
def profile(request):
  return render(request,"profile.html")

def fasilitas(request):
  kamars = Kamar.objects.all()
  return render(request,"fasilitas.html",{"kamars": kamars})