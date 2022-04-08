from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  return render(request, "pages/home.html")

#@login_required
def secret(request):
  return render(request, "pages/secret.html")