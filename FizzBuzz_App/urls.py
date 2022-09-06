from django.urls import path
from . import views

urlpatterns = [
    path('', views.FizzBuzzList.as_view()),
    path('<id>/', views.FizzBuzzDetail.as_view())
]