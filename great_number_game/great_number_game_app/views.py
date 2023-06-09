from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):

    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        print(request.session['number'])

    return render(request, 'index.html')


def guess(request):
    num = request.POST['guess']
    request.session['guess'] = int(num)
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    request.session['attempts'] = int(request.session['attempts']) + 1

    return redirect('/')


def restart(request):
    request.session.clear()

    return redirect('/')
