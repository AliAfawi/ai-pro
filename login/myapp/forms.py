from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Practitioner
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name')
    email = forms.EmailField(max_length=254, required=True, help_text='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
            Student.objects.create(user=user)
        return user

class PractitionerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last name')
    email = forms.EmailField(max_length=254, required=True, help_text='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_practitioner = True
        if commit:
            user.save()
            Practitioner.objects.create(user=user)
        return user
