# Generated by Django 3.2 on 2023-03-23 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='dni',
            new_name='cc',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nit',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pasaporte',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
