# Generated by Django 5.0.1 on 2024-03-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='logo_car',
            field=models.FileField(null=True, upload_to='carreras'),
        ),
    ]
