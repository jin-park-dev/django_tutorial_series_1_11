from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View

from menus.models import Item
from restaurants.models import RestaurantLocation

from .models import Profile

from django.urls import reverse

# Create your views here.

User = get_user_model()


class ProfileFollowToogle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # print(request.data)
        # print(request.POST)
        user_to_toggle = request.POST.get("username").strip()
        # print(user_to_toggle)
        # profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
        # user = request.user
        # if user in profile_.followers.all():
        #     profile_.followers.remove(user)
        # else:
        #     profile_.followers.add(user)
        profile_, is_following = Profile.objects.toggle_follow(request.user, user_to_toggle)

        # return reverse('profiles:detail', kwargs={'slug': 'jinpa'})
        return redirect(f"{profile_.user.username}/")


class ProfileDetailView(DetailView):
    # queryset = User.objects.filter(is_active=True)
    template_name = 'user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # print(context)
        # user = self.get_object()
        user = context['user']
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user).exists()
        qs = RestaurantLocation.objects.filter(owner=user).search(query)
        if items_exists and qs.exists():
            context['locations'] = qs
        return context


"""
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # print(context)
        # user = self.get_object()
        user = context['user']
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user).exists()
        qs = RestaurantLocation.objects.filter(owner=user)
        if query:
            qs = qs.filter(name__icontains=query)
        if items_exists and qs.exists():
            context['locations'] = qs
        return context
"""
