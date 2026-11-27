from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('api/update/tambah/', views.api_tambah_update, name='api_tambah_update'),
    path('api/survei/kirim/', views.api_kirim_survei, name='api_kirim_survei'),
]
