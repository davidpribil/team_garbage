from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calcResults", views.calc_results, name="calc_results"),
]

