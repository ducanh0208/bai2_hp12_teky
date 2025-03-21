"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name = 'home'),
    path('about/', views.about, name = 'about'),
    path('table/', views.table, name = 'table'),
    path('team/', views.team, name = 'team'),
    path('blank/', views.blank, name = 'blank'),
    path('admin_home/', views.admin_home, name= 'admin_home'),
    path('button/', views.button, name = 'button'),
    path('widget/', views.widget, name = 'widget'),
    path('chart/', views.chart, name = 'chart'),
    path('contact/', views.contact, name = 'contact'),
    path('courses/', views.courses, name = 'courses'),
    path('element/', views.element, name = 'element'),
    path('form/', views.form, name = 'form'),
    path('index/', views.index, name = 'index'),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('testimonial/', views.testimonial, name = 'testimonial'),
    path('typography/', views.typography, name = 'typography'),
]
