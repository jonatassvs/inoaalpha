# Generated by Django 4.0.6 on 2022-07-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0003_alter_acaohistorico_date_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acaohistorico',
            name='date_price',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]