import re
from django.shortcuts import render, redirect

from django.views import View
from .models import MapDots


class HomePage(View):
    def get(self, request):
        dots = MapDots.objects.all()
        context = {
            "all_dots": dots
        }
        return render(request, "maps/home_page.html", context=context)

    def post(self, request):
        name = re.sub(",", ".", request.POST.get('name', ''))
        longitute = re.sub(",", ".", request.POST.get('longitute', ''))
        latitude = re.sub(",", ".", request.POST.get('latitude', ''))
        print(name, longitute, latitude)

        if "" not in (name, longitute, latitude):
            maps = MapDots.objects.create(
                name=name, longitute=longitute, latitute=latitude)
            maps.save()
        return redirect("/")


def get_dot(request, dot_id):
    if request.method == "GET":
        specific_dot = MapDots.objects.get(pk=dot_id)
        context = {
            "dot": specific_dot
        }
        return render(request, "maps/get_dot.html", context=context)
    else:
        return HomePage
