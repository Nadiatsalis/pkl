# Generated by Django 3.1.6 on 2021-02-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_uraian_nama_uraian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uraian',
            name='tgl_pembuatan',
            field=models.DateField(),
        ),
    ]