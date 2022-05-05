# Generated by Django 4.0.1 on 2022-04-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('platform', models.CharField(max_length=64)),
                ('year', models.DateField()),
                ('genre', models.CharField(max_length=64)),
                ('publisher', models.CharField(max_length=64)),
                ('na_sales', models.FloatField()),
                ('eu_sales', models.FloatField()),
                ('jp_sales', models.FloatField()),
                ('other_sales', models.FloatField()),
                ('global_sales', models.FloatField()),
            ],
        ),
    ]
