# Generated by Django 3.1.1 on 2020-09-20 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0002_auto_20200920_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='airplane_id',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='ID'),
        ),
    ]
