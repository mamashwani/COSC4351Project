# Users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

group_choices = [('Regular Employee', 'Regular Employee'), ('FINANCE_ADMIN', 'Finance'), 
                ('SALES_ADMIN', 'Sales'), ('HR_ADMIN', 'HR') , ('ENGG_ADMIN', 'Engineering'), ('ADMIN', 'Global')]

class CustomUserCreationForm(UserCreationForm):
    group_name = forms.ChoiceField(required=True, widget=forms.Select, choices=group_choices, )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'group_name', ) #new
        
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'group_name', ) #new