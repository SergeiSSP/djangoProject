from django.core.exceptions import ValidationError




def validate_unique_email(value):
    from .models import Student
    if Student.objects.filter(mail=value).exists():
        raise ValidationError(f'Student with email {value} already exists')
    return value
