# Generated by Django 4.1.7 on 2023-02-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(blank=True, null=True, to='education.lesson', verbose_name='уроки'),
        ),
    ]
