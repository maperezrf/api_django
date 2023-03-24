from django.contrib import admin
from .models import Cliente
# Register your models here

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    '''Admin View for Cliente'''

    list_display = [field.name for field in Cliente._meta.get_fields()]
    search_fields = ('cc','nit','pasaporte')
    ordering = ('-id',)
