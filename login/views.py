from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
import bcrypt

from .models import User, Poke, Poke2 # vamos a trabajar también con clase Poke

# Create your views here.
def login(request):
    return render(request, 'regpoke2.html')

def registrar(request):
    return render(request, 'registro.html')

def inicio3(request):
    # Capturando datos
    nombre = request.POST['nom']
    edad = request.POST['edad']
    mail = request.POST['mail']
    
    poke2 = Poke2.objects.create(
        nombre = nombre,
        edad = edad,
        mail = request.POST['mail'],
    )

    consulta_poke2 = Poke2.objects.all()

    context = {
        'leon': nombre,
        'tigre': edad,
        'puma': mail,
        'jirafa': consulta_poke2,
    }

    return render(request, 'mostrar.html', context)


def inicio2(request):
    # Capturando data desde front
    email2 = request.POST['email2']
    perro = request.POST['perro']
    password = request.POST['password']
    # return HttpResponse(email2+" "+perro+" "+password)

    # Creación en Base Datos del Poke
    # Se crea variable poke
    poke = Poke.objects.create(
        # id no va acá, es automático, es autoincremental solit
        email = email2, 
        # email = request.POST['email2'] otra forma de agregarlo
        perro = request.POST['perro'],
        password = request.POST['password'],     
    ) 

    # Hacemos una consulta que irá a buscar todos los poke desde Base Datos
    lista_pokes = Poke.objects.all()

    context ={
        'gato': email2,
        'elefante': perro,
        'avion': password,
        'pelota': request.POST,
        'lista_pokes': lista_pokes, # va al ciclo for en prueba.html linea 15
        # 'lista_pokes': Poke.objects.all(), es válido también
    }
    return render(request, 'prueba.html', context)


def inicio(request):
    usuario = User.objects.filter(email=request.POST['email'])
    errores = User.objects.validar_login(request.POST, usuario)

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = usuario[0].id
        return redirect('home/')

def registro(request): # para caprturar vairable request se hace request.post['nombrevariable']
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registrar')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password']) # Este post trae todo
        decode_hash_pw = password.decode('utf-8')
        #crear usuario
        if request.POST['rol'] == '1':
            user = User.objects.create(
                nombre=request.POST['nombre'],
                alias=request.POST['alias'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=1,
            )
        else:
            user = User.objects.create(
                nombre=request.POST['nombre'], # Este Post trae algo en especifico
                alias=request.POST['alias'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=2,
            )
        request.session['user_id'] = user.id
    return redirect('home/')

def logout(request):
    request.session.flush()
    return redirect('/')