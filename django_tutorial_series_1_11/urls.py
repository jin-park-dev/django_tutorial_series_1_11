from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset_confirm/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password_reset_done/$', PasswordResetConfirmView.as_view(), name='password_reset_done'),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^items/', include('menus.urls', namespace='menus')),

    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]


