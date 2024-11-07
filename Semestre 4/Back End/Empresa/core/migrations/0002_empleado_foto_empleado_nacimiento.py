# Generated by Django 5.1 on 2024-10-30 17:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='empleado',
            name='nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
