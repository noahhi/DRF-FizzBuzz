from django.urls import path
from . import views

urlpatterns = [
    path('', views.fizzbuzz, name="fizzbuzz"),
    path('<id>/', views.fizzbuzz_detail, name="fizzbuzz_detail")
]