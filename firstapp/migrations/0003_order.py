# Generated by Django 2.1.1 on 2018-10-02 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Pizza', verbose_name='Picca')),
            ],
        ),
    ]
