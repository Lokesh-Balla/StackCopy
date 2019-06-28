from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'enter the username'}),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input is-rounded', 'placeholder': 'enter the password'}),
    )


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'enter the first name'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'enter the last name'})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'enter the user name'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input is-rounded', 'placeholder': 'enter the password'})
    )
