# Generated by Django 4.0.6 on 2022-07-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0014_acaodono_date_buy_alter_acaohistorico_date_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acaodono',
            name='date_buy',
        ),
        migrations.AlterField(
            model_name='acaohistorico',
            name='date_price',
            field=models.TimeField(),
        ),
    ]
