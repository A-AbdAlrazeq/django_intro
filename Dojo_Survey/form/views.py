from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def create_user(request):
    name = request.POST['name']
    city = request.POST['city']
    language = request.POST['Language']
    gender = request.POST['gender']
    comment = request.POST['comment']
    # fetch a value from ['Check'] name,if not exist ,will pass the default value "not checked".
    check = request.POST.get('Check', "not checked")
    context = {
        "name_on_template": name,
        "city_on_template": city,
        "language_on_template": language,
        "gender_on_template": gender,
        "comment_on_template": comment,
        "check_on_template": check,
    }

    return render(request, 'show.html', context)
