# Generated by Django 4.1.1 on 2022-09-16 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('CP', models.DecimalField(decimal_places=1, help_text='ingrese codigo postal', max_digits=6)),
                ('pais', models.CharField(max_length=255)),
                ('activo', models.BooleanField(default=True)),
                
            ],
        ),
    ]
