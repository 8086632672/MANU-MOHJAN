# Generated by Django 3.2.13 on 2022-06-29 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_place_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='img',
            new_name='Img',
        ),
    ]