import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# function based view

#Old can del
"""
def home(request):
    num = None
    some_list = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0, 1000)
    context = {
        "html_var": "**context var**",
        "num": num,
        "bool_item": True,
        "some_list": some_list
    }
    return render(request, "home.html", context)


def about(request):
    context = {
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
    }
    return render(request, "contact.html", context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)
"""


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)

        num = None
        some_list = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        condition_bool_item = False
        if condition_bool_item:
            num = random.randint(0, 1000)
        context = {
            "html_var": "**context var**",
            "num": num,
            "bool_item": True,
            "some_list": some_list
        }

        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"


