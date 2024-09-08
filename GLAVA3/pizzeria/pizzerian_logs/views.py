from django.shortcuts import render, get_object_or_404
from .models import Pizza
# Create your views here.
def index(request):
    return render(request, 'pizzerian_logs/index.html')

def pizza(request):
    pizza = Pizza.objects.order_by('name')
    context = {'pizza': pizza}
    return render(request, 'pizzerian_logs/pizza.html', context)

def toping(request, toping_id):
    toping = Pizza.objects.get(id=toping_id)
    entries = toping.toppings.order_by('-toppings')
    context = {'toping': toping, 'entries': entries}
    return render(request, 'pizzerian_logs/topings.html', context)