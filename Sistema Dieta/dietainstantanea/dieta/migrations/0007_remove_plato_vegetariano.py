# Generated by Django 2.0.6 on 2018-11-25 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '0006_auto_20181125_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plato',
            name='vegetariano',
        ),
    ]
