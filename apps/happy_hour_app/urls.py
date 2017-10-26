from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^search$', views.search, name="search"),
    url(r'^search_results$', views.results, name="search_results"),
    url(r'restaurant/(?P<restaurant_id>\d+)/$', views.restaurant, name="restaurant")
]
