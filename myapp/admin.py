from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PC, Composant

admin.site.register(PC)
admin.site.register(Composant)
