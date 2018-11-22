from django import forms
import re
from django.core.validators import RegexValidator




class UserRegForm(forms.Form):
        my_validator = RegexValidator(r"A", "Your string should contain letter A in it.")

        username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
            "placeholder":"Username",
            "pattern":"[[^A-Za-z0-9]{3,15}",
            "title":"Usernames must be between 3 and 15 characters. Only letters and numbers are allowed"
        }))
        password = forms.CharField(label='Password',max_length=32, widget=forms.PasswordInput(attrs={
            "placeholder":"Enter password",
            "pattern":"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
            "title":"Password must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
        }))
        re_password = forms.CharField(label='Repeat Password',max_length=32, widget=forms.PasswordInput(attrs={
            "placeholder":"Repeat password"}))

        def clean_password(self):
            pass_passed=self.cleaned_data.get('password')
            pass2_passed=self.cleaned_data.get('re_password')
            if pass_passed != pass2_passed:
                raise forms.ValidationError("Passwords do not match")
            return pass_passed



class UserLogInForm(forms.Form):
        username = forms.CharField(label='Username', min_length=2,max_length=15, widget=forms.TextInput(attrs={
        "placeholder":"Username"}))
        password = forms.CharField(label='Password', min_length=8,max_length=32, widget=forms.PasswordInput(attrs={
        "placeholder":"Password"}))

class UserProfile(forms.Form):
        username = forms.CharField(label='Enter your username', max_length=100)
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)
        re_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
        email=forms.EmailField()
        hobbies=forms.CharField(widget=forms.Textarea)
