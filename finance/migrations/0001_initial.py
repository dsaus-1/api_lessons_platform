# Generated by Django 4.1.7 on 2023-03-03 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0007_alter_course_price_alter_lesson_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payment', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('payment_sum', models.FloatField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('money transfer', 'перевод на счет')], max_length=30, verbose_name='способ оплаты')),
                ('status', models.CharField(choices=[('created', 'создан'), ('confirmed', 'подтвержден')], default='created', max_length=20, verbose_name='Статус оплаты')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка на оплату')),
                ('payment_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='оплаченный курс')),
                ('payment_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
