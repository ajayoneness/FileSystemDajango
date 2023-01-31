from django.shortcuts import render, HttpResponse
import json
from .models import Message


def codeAj(request):
    return HttpResponse("<h1>Hi, Ajay </h1>")


def get_bot_response(request):
    userText = request.args.get('msg')
    print(userText)
    return str("i am ajay")