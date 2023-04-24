# Generated by Django 4.1.8 on 2023-04-21 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GeneroLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('edicion', models.IntegerField()),
                ('year_publicacion', models.IntegerField()),
                ('fotolibro', models.ImageField(upload_to='fotos')),
                ('resumen', models.TextField()),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.autor')),
                ('id_editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.editorial')),
                ('id_genero_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.generolibro')),
                ('id_idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.idioma')),
            ],
        ),
    ]
