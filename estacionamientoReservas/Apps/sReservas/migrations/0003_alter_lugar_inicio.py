# Generated by Django 4.1.3 on 2022-12-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sReservas', '0002_remove_lugar_ola_alter_lugar_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='inicio',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
