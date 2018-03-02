from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.aboutpageview.as_view(), name = 'about')
]