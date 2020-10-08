from django.shortcuts import render, redirect
from .models import *
import requests


def index(request):
    return render(request, 'index.html')


def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        msg = request.POST['msg']
        Register.objects.create(name=name,
                                last_name=last_name,
                                email=email)
        ides = [833143574, 744526447, ]
        text = "New user to ITstation\n\nName: "+name+"\nLast name: "+last_name+"\nEmail: "+email+"\nMessage: "+msg
        url = 'https://api.telegram.org/bot1307280045:AAEUSAT3v_rx-zg-znDQ1utvLGyOCr5d-m8/sendMessage?chat_id='
        for i in ides:
            requests.get(url + str(i) + '&text=' + text)
        return redirect('index')
    else:
        return render(request, 'index.html')