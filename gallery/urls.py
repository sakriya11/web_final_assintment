from django.urls import path

from gallery import views

urlpatterns=[
    path('',views.show),
    path('delete/<pid>',views.delete)
]