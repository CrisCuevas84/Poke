from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errores = {}
        if len(User.objects.filter(email=postData['email'])) > 0:
            errores['existe'] = "Email ya registrado"
        else:
            if len(postData['nombre']) == 0:
                errores['nombre'] = "Nombre es obligatorio"
            if len(postData['alias']) == 0:
                errores['alias'] = "Alias es obligatorio"
            EMAIL = re.compile(
                r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL.match(postData['email']):
                errores['email'] = "email invalido"
            if len(postData['password']) < 6:
                errores['password'] = "Password debe ser mayor a 6 caracteres"
            if postData['password'] != postData['password2']:
                errores['password'] = "Password no son iguales"
        return errores

    def encriptar(self, password):
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return password

    def validar_login(self, postData, usuario ):
        errores = {}
        if len(usuario) > 0:
            pw_given = postData['password']
            pw_hash = usuario[0].password

            if bcrypt.checkpw(pw_given.encode(), pw_hash.encode()) is False:
                errores['pass_incorrecto'] = "password es incorrecto"
        else:
            errores['usuario_invalido'] = "Usuario no existe"
        return errores

class User(models.Model):
    nombre = models.CharField(max_length=40)
    alias = models.CharField(max_length=40) # Pide alias en poke
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    cumple = models.DateTimeField() # Como pide cumpleaños en examen poke, esta fecha la pasamos desde el html no usar autonow ya que cada vez que usuario modifica actualiza fecha.
    rol = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Nueva clase
class Poke(models.Model):
    id = models.AutoField(primary_key=True) # Creará un campo autoincremental primario
    email = models.CharField(max_length=60) # Charfield para los de tipo string
    perro = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Poke2(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    edad = models.CharField(max_length=3)
    mail = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)