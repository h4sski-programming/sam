from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    status = models.BooleanField(null=False, default=False)

    def __repr__(self) -> str:
        return f'Module(id={self.id}, name={self.name}, status={self.status})'

    def ___str___(self) -> str:
        return f'Module(id={self.id}, name={self.name}, status={self.status})'
    

class TestModel(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self) -> str:
        return self.name