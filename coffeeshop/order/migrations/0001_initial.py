# Generated by Django 5.0.4 on 2024-04-22 17:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_image_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('1', 'ثبت شده'), ('2', 'در حال آماده سازی'), ('3', 'آماده'), ('4', 'تحویل داده شده')])),
                ('des', models.TextField()),
                ('orders', models.ManyToManyField(to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
