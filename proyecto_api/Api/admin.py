from django.contrib import admin
from Api import models

# Register your models here.

admin.site.register(models.UserProfile)

admin.site.register(models.Cerveza)

admin.site.register(models.Botella)

admin.site.register(models.Contact)
