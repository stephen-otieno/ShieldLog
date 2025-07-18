from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="landing_page"),
    path('homepage/', views.homepage, name= "homepage")
]