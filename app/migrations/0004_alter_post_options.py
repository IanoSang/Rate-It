# Generated by Django 4.0.5 on 2022-06-15 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
    ]
