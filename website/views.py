from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    data = {
        'cool_title': '😂this title is coming from python😂'
    }
    return render(request, 'index.html', data)
