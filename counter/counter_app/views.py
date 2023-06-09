from django.shortcuts import render, redirect


def index(request):
    if 'count' and 'counter' not in request.session:
        request.session['count'] = 1
        request.session['counter'] = 1
    else:
        request.session['count'] += 1
        request.session['counter'] += 1
    context = {
        "count": request.session['count'],
        "real_count": request.session['counter'],

    }

    return render(request, "index.html", context)


def reset(request):
    request.session.clear()
    return redirect('/')


def add_two(request):
    request.session['count'] += 1
    return redirect('/')


def user_number(request):
    num = request.POST['number']
    if num == "":
        num = 0
    else:
        request.session['number'] = request.POST['number']
        request.session['count'] += int(num)-1

    return redirect('/')
