from django import forms
from django.core.validators import RegexValidator

class MyForm(forms.Form):
    ip = forms.CharField(
        max_length=30,
        required=True,
            validators=[
                RegexValidator(
                    regex=r'^[a-zA-Z0-9]*$',
                    message=('Error'),
                ),
            ]
        )