from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password_verify = forms.CharField(label='Password Verification', max_length=128, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]
        widgets = {
                'name': forms.TextInput(),
                'email': forms.EmailInput(),
                'password': forms.PasswordInput(),
                }
        help_text = {
                'name': _('Choose a nice username.'),
                }
        error_messages = {
                'name': {
                    'max_length': _('Username is too long.'),
                    },
                'email': {
                    'invalid': _('Enter a valid email address.'),
                    },
                'password': {
                    'invalid': _('Passwords should be 8 character long and not be entirely numeric.'),
                    },
                }


    def clean(self):
        cleaned_data = super().clean()
        if not 'password' in cleaned_data:
            raise ValidationError(
                    _('Password field can not be empty.'), code='required')
        if cleaned_data['password_verify'] != cleaned_data['password']:
            raise ValidationError(
                    _('Password does not match the verification.'), code='mismatch')
        validate_password(cleaned_data['password'])

