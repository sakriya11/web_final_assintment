from django.urls import path

from Home import views

urlpatterns = [
    path("", views.show),
    path('home/', views.show),
    path("register/", views.register),
    path("login/", views.login),
    path("user/",views.user),
    path("logout/",views.logout)
]
