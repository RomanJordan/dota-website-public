from django.urls import path
from .views import HeroPageView, HeroDetailView


urlpatterns = [
    path('', HeroPageView.as_view(), name='home'),
    path('heroes/<str:slug>/', HeroDetailView.as_view(), name='hero-details'),

]