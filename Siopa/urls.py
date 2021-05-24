from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
]
