# Generated by Django 4.2.1 on 2023-05-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam_app', '0002_alter_module_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
