# Generated by Django 4.1.7 on 2023-03-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_alter_payment_payment_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('created', 'создан'), ('confirmed', 'подтвержден'), ('rejected', 'отклонен')], default='created', max_length=20, verbose_name='Статус оплаты'),
        ),
    ]
