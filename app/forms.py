from django import forms
from django.core.exceptions import ValidationError

from .models import Client


def validate_schema_name(value):
    # Add your custom validation logic here
    # For example, check if the schema name is valid according to your requirements
    if not value.isalnum():  # You can adjust this validation based on your needs
        raise ValidationError("Invalid characters in the schema name.")


class ClientRegistrationForm(forms.ModelForm):
    schema_name = forms.CharField(max_length=100, validators=[validate_schema_name])

    class Meta:
        model = Client
        fields = ['name', 'schema_name']
