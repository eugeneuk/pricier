# Generated by Django 3.2.8 on 2021-11-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='start_from',
            field=models.IntegerField(null=True),
        ),
    ]
