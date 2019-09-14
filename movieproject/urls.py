"""movieproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from movieapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'^index/',views.index),
    url(r'^login/', views.usrlog),
    url(r'^home/', views.homeapi),
    url(r'^registration/', views.registration),
    url(r'^movies/', views.movies),
    url(r'^search/', views.searchmovie),
    url(r'^userlogout/',views.userlogout),
    url(r'^user-details/',views.userdetails),
    url(r'^movie-data/',views.movie_details),
    url(r'^movie-details/',views.allmovie),
    url(r'^book/',views.booking),
    url(r'^show/',views.book),
    url(r'^seat-book/',views.seats),
    url(r'^selection/',views.selection),
    url(r'^trans/',views.trans),
    url(r'^book-seat/',views.book_seat),
    url(r'^selected/',views.selected),
    url(r'^myprofile/',views.details),
]
