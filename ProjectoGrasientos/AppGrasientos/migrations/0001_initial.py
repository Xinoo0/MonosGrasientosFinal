# Generated by Django 4.1.2 on 2023-07-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('modelo', models.CharField(max_length=25)),
                ('marca', models.CharField(max_length=25)),
                ('precio', models.CharField(max_length=10)),
            ],
        ),
    ]
