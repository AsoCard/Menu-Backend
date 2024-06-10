# Generated by Django 4.0.10 on 2024-06-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'ثبت شده'), ('2', 'در حال آماده سازی'), ('3', 'آماده'), ('4', 'تحویل داده شده')], default='1', max_length=100),
        ),
    ]