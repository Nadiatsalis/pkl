# Generated by Django 3.1.6 on 2021-02-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uraian',
            name='nama_uraian',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]