# Generated by Django 4.0.6 on 2022-07-25 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0011_alter_acaohistorico_date_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acaodono',
            old_name='buy_price',
            new_name='price',
        ),
        migrations.AddField(
            model_name='acaodono',
            name='date_buy',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
