# Generated by Django 4.1.1 on 2022-10-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('CP', models.DecimalField(decimal_places=1, help_text='ingrese codigo postal', max_digits=6)),
                ('pais', models.CharField(max_length=255)),
                ('activo', models.BooleanField(default=True)),
                ('Creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('website', models.URLField(max_length=250)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Inmueble',
        ),
    ]