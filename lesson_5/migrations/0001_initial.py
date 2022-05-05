# Generated by Django 4.0.1 on 2022-04-11 11:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(null=True)),
                ('delivered_at', models.DateTimeField(auto_now_add=True)),
                ('could_use_in_bouquet', models.BooleanField(default=True)),
                ('Wikipedia', models.URLField(default='https://www.wikipedia.org/', unique_for_date='delivered_at')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('invoice', models.FileField(upload_to='')),
                ('user_uuid', models.UUIDField(editable=False)),
                ('discount_size', models.DecimalField(decimal_places=5, max_digits=5)),
                ('client_ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fresh_period', models.DurationField(default=datetime.timedelta(days=5), help_text='Use this field when you need to have information about bouquet fresh time')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField(default=1.0)),
                ('flowers', models.ManyToManyField(to='lesson_5.Flower', verbose_name='This bouquet consists of this flowers')),
            ],
        ),
    ]
