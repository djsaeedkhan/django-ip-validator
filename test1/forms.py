from django import forms
from django.core.validators import RegexValidator, EmailValidator, validate_ipv46_address
validate_hostname = RegexValidator(regex=r'[a-zA-Z0-9-_]*\.[a-zA-Z]{2,6}')

my_validator = RegexValidator(r'[a-zA-Z0-9-_]*\.[a-zA-Z]{2,6}', "Your string should contain letter A in it.")

class CacheCheck(forms.Form):
    ip = forms.CharField(max_length=100,validators=[my_validator])
