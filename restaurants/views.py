import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocation
from .forms import ResaurantCreateForm, RestaurantLocationCreateForm

# Create your views here.
# function based view

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print('Rest_list_view slug: '.format(slug))
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all() # Can filter by user


# This works with forms.ModelForm to auto do saving aspect
class RestaurantCreateView(LoginRequiredMixin, CreateView):
    # login_url = '/lgin/'

    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    # success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context