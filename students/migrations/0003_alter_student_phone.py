# Generated by Django 4.1.1 on 2022-10-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, db_column='phone_number', max_length=13, null=True, verbose_name='Phone number'),
        ),
    ]
