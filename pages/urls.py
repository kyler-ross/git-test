from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.aboutpageview.as_view(), name = 'about'),
    path('Project 1/', views.project1pageview.as_view(), name = 'Project 1'),
    path('Project 2/', views.project2pageview.as_view(), name = 'Project 2'),
    path('Project 3/', views.project3pageview.as_view(), name = 'Project 3')
]