# Generated by Django 5.1.2 on 2024-11-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_datosextra'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='avatar',
            field=models.ImageField(blank=True, default='mascotas/default-image.jpg', null=True, upload_to='mascotas'),
        ),
        migrations.DeleteModel(
            name='DatosExtra',
        ),
    ]
