# Generated by Django 2.0.7 on 2020-09-05 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_serviceprovider_cordinate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='owner',
        ),
        migrations.DeleteModel(
            name='serviceProvider',
        ),
    ]
