from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="landing_page"),
    path('homepage/', views.homepage, name= "homepage"),
    path('login/', views.login_page, name= "login"),
    path('signup/', views.signup_page, name="signup")
]