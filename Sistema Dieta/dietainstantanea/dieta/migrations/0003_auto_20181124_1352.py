# Generated by Django 2.0.6 on 2018-11-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0002_ingrediente_nomingrediente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='cantidad',
            field=models.CharField(max_length=10),
        ),
    ]
