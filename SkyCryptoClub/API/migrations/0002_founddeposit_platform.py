# Generated by Django 3.0.8 on 2020-07-16 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='founddeposit',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.Platform'),
            preserve_default=False,
        ),
    ]