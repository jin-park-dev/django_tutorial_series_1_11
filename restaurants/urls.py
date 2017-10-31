from django.conf.urls import url



from .views import (
    # restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    # restaurant_createview,
    RestaurantCreateView
)

urlpatterns = [

    url(r'^$', RestaurantListView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),

]

