# Generated by Django 5.0 on 2023-12-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsTasks', '0025_estudiante_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.FloatField(default=0.0, max_length=10),
        ),
    ]
