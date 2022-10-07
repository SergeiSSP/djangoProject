from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import ValidEmailDomain  # validate_unique_email

VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com', '@test.com')


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
        validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)],
    )
    phone = models.CharField(
        max_length=13,
        verbose_name='Phone number',
        db_column='phone_number',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'students'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            mail = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            st = cls(first_name=first_name, last_name=last_name, mail=mail, birthday=birthday)
            try:
                st.full_clean()
                st.save()
            except:
                print(f'Incorrect data{first_name}{last_name}{mail}{birthday}')
