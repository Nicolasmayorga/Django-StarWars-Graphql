# Generated by Django 3.0.5 on 2020-06-14 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Personajes', models.TextField()),
                ('episodio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='peliculas.Peli')),
            ],
        ),
    ]
