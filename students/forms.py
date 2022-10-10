from django import forms

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
        cleaned_value = ''.join([i for i in value if not i.isalpha()])
        return cleaned_value

