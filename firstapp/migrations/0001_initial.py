# Generated by Django 2.1.1 on 2018-09-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Pizza')),
                ('description', models.TextField(verbose_name='description pizza')),
                ('rating', models.FloatField(default=0, verbose_name='rating pizza')),
                ('url', models.URLField(verbose_name='url pizza')),
            ],
        ),
    ]
