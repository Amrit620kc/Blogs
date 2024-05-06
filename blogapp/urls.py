from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #For Html page
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("blog/",views.blog, name="blog"),
    path("contact/",views.contact, name="contact"),
    path('show_more/<slug:url>/',views.show_more, name="show_more"),
    path('search/',views.search, name="search"),

    #For authentication
    path('signup/',views.signup, name='signup'),
    path("login/",views.login, name='login'),
    path('logout/',views.logout, name="logout"),
    #For comment
    path('comment/',views.commentt, name="commentt"),
]
