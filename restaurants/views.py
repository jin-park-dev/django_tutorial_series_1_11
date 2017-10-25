import random

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation

# Create your views here.
# function based view

#Old can del
'''
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

# Now inside URL in one line
"""
class AboutView(TemplateView):
    template_name = "about.html"


class ContactTemplateView(TemplateView):
    template_name = "contact.html"
"""
'''

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, *args,**kwargs):
        print(self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id is also same.
        return obj