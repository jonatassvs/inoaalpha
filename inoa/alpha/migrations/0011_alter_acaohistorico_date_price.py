# Generated by Django 4.0.6 on 2022-07-25 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0010_remove_acaodono_date_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acaohistorico',
            name='date_price',
            field=models.DateTimeField(),
        ),
    ]