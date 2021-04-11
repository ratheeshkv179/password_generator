from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, "generator/home.html")

def password(request):

    letters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("number") == "on":
        letters  += list("0123456789")
    if request.GET.get("special") == "on":
        letters += list("~!@#$%^&*()")
    if request.GET.get("alpha") == "on":
        letters += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    password_generated = ""
    for val in range(int(request.GET.get("length"))):
        password_generated += random.choice(letters)
    return render(request, "generator/password.html", {"password": password_generated})