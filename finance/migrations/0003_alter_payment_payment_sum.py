# Generated by Django 4.1.7 on 2023-03-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_payment_payment_id_tinkoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_sum',
            field=models.IntegerField(verbose_name='сумма оплаты'),
        ),
    ]
