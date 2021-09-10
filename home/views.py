from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['user_id']) # bucas la info en la base de datos
    numero = 1984
    context = {                     
        "active_user": reg_user,
        "avion": numero,
    } # Estamos yendo a buscar al usuario, un valor desde el backend al frontend es un objeto

    return render(request, 'home.html', context) # Detecta que va la variable active_user (trae todo el user)
