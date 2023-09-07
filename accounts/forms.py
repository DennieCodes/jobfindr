from django import forms

class SignupForm(forms.Form):
  email = forms.EmailField(max_length=150)
  password = forms.CharField(
    max_length=150,
    widget=forms.PasswordInput
  )
  password_confirmation = forms.CharField(
    max_length=150,
    widget=forms.PasswordInput
  )

class LoginForm(forms.Form):
  email = forms.EmailField(max_length=150)
  password = forms.CharField(
    max_length=150,
    widget=forms.PasswordInput
  )