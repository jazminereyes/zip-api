# Generated by Django 3.1.1 on 2020-09-20 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='airplane_id',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='ID'),
        ),
    ]
