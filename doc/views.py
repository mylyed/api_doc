from django.shortcuts import render
from django.http import HttpResponse
from doc.models import *
import json


# Create your views here.
def index(requsest):
    all_ = Platform.objects.all()
    return render(requsest, 'doc.html', {'all': all_})


def api(requsest, api_id):
    api_ = Api.objects.filter(id=api_id)[0]
    return render(requsest, 'details.html', {'api': api_})
