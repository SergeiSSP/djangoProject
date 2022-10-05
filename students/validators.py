from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_unique_email(value):
    from .models import Student
    if Student.objects.filter(mail=value).exists():
        raise ValidationError(f'Student with email {value} already exists')
    return value


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f"Invalid Email Address. The domain <{args[0].split('@')[1]}> not valid.")