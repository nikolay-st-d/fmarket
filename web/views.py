from http.client import HTTPResponse

from django.shortcuts import render
from django.urls import include


def index(request):
    context = {
        "h1": "Farmer's Market",
        "h2": "Sell or Buy Farmer's pure and tasty food!"
    }
    return render(request, 'base.html', context=context)
