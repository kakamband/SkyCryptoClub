# Generated by Django 3.0.8 on 2020-07-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20200721_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='is_global',
            field=models.BooleanField(default=False),
        ),
    ]