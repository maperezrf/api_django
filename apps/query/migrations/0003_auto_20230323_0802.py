# Generated by Django 3.2 on 2023-03-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_auto_20230322_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cc',
            field=models.PositiveBigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=models.PositiveBigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pasaporte',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]