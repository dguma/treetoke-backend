from django.contrib import admin
from .models import Strains

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'password')

admin.site.register(Strains)