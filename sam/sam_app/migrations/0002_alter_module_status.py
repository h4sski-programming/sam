# Generated by Django 4.2.1 on 2023-05-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
