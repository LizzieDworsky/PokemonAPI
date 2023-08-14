from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_pokemon),
    path('<int:pk>', views.pokemon_by_id)
]