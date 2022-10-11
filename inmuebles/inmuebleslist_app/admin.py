from django.contrib import admin

# Register your models here.
from inmuebleslist_app.models import Edificacion, Empresa
admin.site.register(Edificacion)
admin.site.register(Empresa)