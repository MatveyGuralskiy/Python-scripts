from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<center><h2>My First Page from Python DJANGO! </h2></center>")