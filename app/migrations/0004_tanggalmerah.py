# Generated by Django 3.1.6 on 2021-02-20 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210208_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='TanggalMerah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_merah', models.DateField()),
            ],
        ),
    ]