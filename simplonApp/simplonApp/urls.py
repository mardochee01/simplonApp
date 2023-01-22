from django.contrib import admin
from django.urls import path
from participant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registration, name='registration'),
    path('list-participant/', views.show, name='show')
]
