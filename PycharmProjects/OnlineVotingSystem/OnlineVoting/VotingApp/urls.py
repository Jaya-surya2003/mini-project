
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('registration/', views.registration, name='registration'),
    path('vote/', views.vote, name='vote'),
    path('can/', views.can, name='can'),
    path('result/', views.result, name='result'),

]

