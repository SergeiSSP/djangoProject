from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'mail',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        cleaned_value = value.lower().capitalize()
        return cleaned_value

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        cleaned_value = value.lower().capitalize()
        return cleaned_value


    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        try:
            cleaned_value = ''.join([i for i in value if not i.isalpha()])
            if len(cleaned_value) < 10:
                raise ValidationError(f'Phone number{cleaned_value} is too short')
            else:
                return cleaned_value
        except TypeError:
            return value



class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone',
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
