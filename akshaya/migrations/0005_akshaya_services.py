# Generated by Django 4.2.1 on 2023-05-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akshaya', '0004_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='akshaya',
            name='services',
            field=models.ManyToManyField(to='akshaya.service'),
        ),
    ]
