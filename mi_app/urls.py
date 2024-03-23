from django.urls import path
from .views import Hello_world

urlpatterns = [
    # define la ruta para la vista hello_world.
    path('hello/', Hello_world)
]