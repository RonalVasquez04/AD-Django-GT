# Generated by Django 4.2.7 on 2023-12-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentsTasks', '0006_nota_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.FloatField(default=0.0, max_length=10),
        ),
    ]