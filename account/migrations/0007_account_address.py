# Generated by Django 2.2.2 on 2021-12-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20211223_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default='Nan', max_length=300),
        ),
    ]
