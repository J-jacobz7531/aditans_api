# Generated by Django 2.0.7 on 2020-09-06 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20200906_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='name',
            new_name='owner',
        ),
    ]
