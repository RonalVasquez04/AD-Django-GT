# Generated by Django 5.0 on 2023-12-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsTasks', '0017_alter_entregatarea_fechaentrega'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='archivo',
        ),
        migrations.AddField(
            model_name='entregatarea',
            name='archivo',
            field=models.FileField(null=True, upload_to='entregas/'),
        ),
    ]
