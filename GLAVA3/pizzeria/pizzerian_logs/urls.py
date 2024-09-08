from django.urls import path

from . import views

app_name = 'pizzerian_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas', views.pizza, name='pizza'),
    path('pizzas/<int:toping_id>/', views.toping, name='toping'),
    ]