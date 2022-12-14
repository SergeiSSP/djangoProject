# Generated by Django 4.1.1 on 2022-10-10 13:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teachers_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'First name must be greater than 1 character')], verbose_name='First name')),
                ('last_name', models.CharField(db_column='last_name', max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'First name must be greater than 1 character')], verbose_name='Last_name')),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, db_column='phone_number', max_length=13, null=True, verbose_name='Phone number')),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
