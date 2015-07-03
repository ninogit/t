from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from bs4 import BeautifulSoup
from .models import Shop
from django.forms.models import model_to_dict

# Create your views here.

def find_product(request):
    return HttpResponse('work')