# Generated by Django 4.2.7 on 2023-12-15 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsTasks', '0018_remove_tarea_archivo_entregatarea_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='birthdate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='direccion',
            field=models.CharField(default='', max_length=100),
        ),
    ]