import time

from django.shortcuts import render, redirect
from grove_servo import GroveServo

# Create your views here.
def home(request):
     return render(request,'home.html')

def rotate(request):
     degree = int(request.POST['degree'])
     servo = GroveServo(5)

     servo.setAngle(degree)
     time.sleep(0.05)     

     return redirect('main')