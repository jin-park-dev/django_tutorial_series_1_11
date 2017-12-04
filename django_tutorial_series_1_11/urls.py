from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, LogoutView


from profiles.views import ProfileFollowToogle, RegisterView, activate_user_view
from menus.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^u/$', ProfileFollowToogle.as_view(), name='follow'),


    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset_confirm/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^password_reset_done/$', PasswordResetConfirmView.as_view(), name='password_reset_done'),

    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('menus.urls', namespace='menus')),

    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]


