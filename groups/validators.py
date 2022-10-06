from django.core.exceptions import ValidationError
import datetime

def validate_start_date(value):
    if value < datetime.date.today():
        raise ValidationError(
            ('%(value)s is not a valid start date'),
            params={'value': value},
        )