from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models

from .validators import validate_unique_email


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First Name',
        db_column='first_name',
        validators=[MinLengthValidator(2, "First name must be greater than 1 character")]
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last Name',
        db_column='last_name',
        validators=[MinLengthValidator(2, "Last name must be greater than 1 character")],
        error_messages={'min_length': 'Last name must be greater than 1 character'}
    )
    birthday = models.DateField(default=date.today,
                                null=True,
                                blank=True)
    mail = models.EmailField(
        null=True,
        validators=[validate_unique_email],
    )


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'students'