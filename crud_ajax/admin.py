from django.contrib import admin

# Register your models here.
from .models import CrudUser

class CrudUseradmin(admin.ModelAdmin):
    fields = ['name', 'address', 'age']


admin.site.register(CrudUser, CrudUseradmin)