from django.urls import path
from . import views

urlpatterns = [
# path('', views.homePageView, name='home'),
path('', views.landingpage, name='home'),
]