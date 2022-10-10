# Generated by Django 4.1.1 on 2022-10-05 21:16

import datetime
import django.core.validators
from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'First name must be greater than 1 character')], verbose_name='First Name')),
                ('last_name', models.CharField(db_column='last_name', error_messages={'min_length': 'Last name must be greater than 1 character'}, max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Last name must be greater than 1 character')], verbose_name='Last Name')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('mail', models.EmailField(max_length=254, null=True, validators=[students.validators.ValidEmailDomain('@gmail.com', '@yahoo.com', '@test.com')])),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
