"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    #path('admin/', admin.site.urls),
    path("reservationshow",views.showreservation,name="showreservation"),
    path("reservationaddnew",views.addnewreservation,name="adduser"),
    path("editres/<int:id>",views.editreservation,name="edit"),
    path("updateres/<int:id>",views.updatereservation,name="update"),
    path("deleteres/<int:id>",views.deletereservation,name="delete"),
    path("user",views.index2,name="index2"),
    path("clients",views.Clients,name="clients"),
    path("adduser",views.SignupPage,name="adduser"),
    path("about",views.About,name="about"),
    path("blog-single",views.BlogSingle,name="blog-single"),
    path("blog",views.Blog,name="blog"),
    path("car-single/<int:id>",views.CarSingle,name="car-single"),
    path("car",views.Car,name="car"),
    path("contact",views.Contact,name="contact"),
    #path("pricing",views.Pricing,name="pricing"), 
    path("services",views.Services,name="services"), 
    path("home", views.home, name='home'),
    path("", views.home, name='home'),
    path("addnew",views.addnew,name="addnew"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete"),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutPage,name='logout'),
    path('rent-a-car/',views.rent_a_car,name='rent-a-car'),
    path('scraptitle/', views.get_title, name='scraptitle'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

