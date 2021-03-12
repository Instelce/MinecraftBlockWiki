from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.home, name="home"),
    path('block_page/', views.block_page, name="block_page")
]