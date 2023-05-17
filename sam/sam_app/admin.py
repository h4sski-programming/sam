from django.contrib import admin

# Register your models here.
from .models import Module, TestModel

admin.site.register(Module)
admin.site.register(TestModel)