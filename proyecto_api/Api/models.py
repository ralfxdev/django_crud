from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Falta email valido')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objet = UserProfileManager()

# Campo requerito para el login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

# creamos las funciones
    def get_fullname(self):
        return self.name

    def __str__(self):
        return self.email

class Cerveza(models.Model):
    marca = models.CharField(max_length=50)
    alcohol = models.DecimalField(max_digits=4,decimal_places=2)
    es_artesanal= models.BooleanField(default=False)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    creado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True)


    def __str__(self):
        return self.marca


# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

#     def __str__(self):
#         return self.name
    

class Botella(models.Model):
    marca = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    capacidad = models.DecimalField(max_digits=4,decimal_places=2)
    color = models.CharField(max_length=25,default="Transparente")
    altura = models.CharField(max_length=10)

    def __str__(self):
        return self.marca