# Generated by Django 4.0.6 on 2022-07-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0006_alter_acaodono_date_buy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
