from django.shortcuts import render, redirect
from .models import *
from django.http import *
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def p_data(request):
    obj = ngo_list.objects.all()  # .order_by('-date')
    # print(obj)
    return render(request, 'data.html', {'obj': obj})


@method_decorator(csrf_exempt, name='dispatch')
@requires_csrf_token
def p_help(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        district = request.POST.get("district")
        city = request.POST.get("city")
        state = request.POST.get("state")
        food = request.POST.get("food")
        sanitizer = request.POST.get("sanitizer")
        medical_supply = request.POST.get("medical supply")
        contact = request.POST.get("Contact")
        people = request.POST.get("people")
        form1 = person_help()

        form1.name = name
        form1.district = district
        form1.city = city
        form1.state = state
        form1.people = people

        if food == "True":
            form1.food = food
        else:
            form1.food = "False"

        if sanitizer == "True":
            form1.sanitizer = sanitizer
        else:
            form1.sanitizer = "False"

        if medical_supply == "True":
            form1.medical_supply = medical_supply
        else:
            form1.medical_supply = "False"
        form1.contact = contact
        form1.save()
        if form1.state == "Delhi" or form1.state == "delhi":
            print(form1.state)
            # p_data(request)
            obj = ngo_list.objects.ngo_name
            return render(request, 'data.html', {'obj': obj})
        # return render(request, 'form.html')

    return render(request, 'form.html')


def corona_virus_helpdesk(request):
    return render(request, 'corona virus helpdesk.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def helplineno(request):
    return render(request, 'helplineno.html')


def helpus(request):
    return render(request, 'helpus.html')


def login_page(request):
    return render(request, 'login_page.html')


def map(request):
    return render(request, 'map.html')


def map2(request):
    return render(request, 'map2.html')


def states(request):
    return render(request, 'states.html')


def needhelp(request):
    return render(request, 'form.html')
