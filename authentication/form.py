from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User

class UserForm(forms.ModelForm):
    password_verify = forms.CharField(label='Password Verification', required=False, max_length=128, widget=forms.PasswordInput())
    field_order = ['username', 'email', 'password', 'password_verify']

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]
        widgets = {
                'username': forms.TextInput(),
                'email': forms.EmailInput(),
                'password': forms.PasswordInput(render_value=True),
                }
        error_messages = {
                'username': {
                    'required': _('Username is required.'),
                    },
                'email': {
                    'invalid': _('Enter a valid email address.'),
                    'required': _('email is required.'),
                    },
                'password': {
                    'required': _('Password is required.'),
                    },
                }

    def clean(self):
        cleaned_data = super().clean()
        username_flag, email_flag, pass_flag, verify_flag = False, False, False, False
        if not 'password' in cleaned_data:
            pass_flag = True
        if not 'password_verify' in cleaned_data:
            verify_flag = True
        if not 'username' in cleaned_data:
            username_flag = True
        if not 'email' in cleaned_data:
            email_flag = True

        '''
        Password validation part
        '''
        err_list = []
        if not pass_flag and not verify_flag and cleaned_data['password_verify'] != cleaned_data['password']:
            err_list.append(ValidationError(
                    _('Password does not match the verification.'),
                    code='mismatch'))
        if not pass_flag:
            try:
                validate_password(cleaned_data['password'])
            except ValidationError as err:
                err_list.append(ValidationError(
                    _('Passwords should be 8 character long and not be entirely numeric.'),
                    code='invalid'))
        if err_list:
            self.add_error('password', ValidationError(err_list))
        
        '''
        Uniqueness validation part
        '''
        if not username_flag and User.objects.filter(username=cleaned_data['username']).exists():
            self.add_error('username', ValidationError(
                _('Username already exists.'),
                code='exists'))
        if not email_flag and User.objects.filter(email=cleaned_data['email']).exists():
            self.add_error('email', ValidationError(
                _('Email already exists.'),
                code='exists'))


