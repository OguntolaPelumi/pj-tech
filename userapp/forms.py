from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Contact_message

position = [
        ("", ""),
        ("CEO", "CEO"),
        ("GMD", "GMD"),
        ("CTO", "CTO"),
        ("Supervisor", "Supervisor"),
        ("Accountant", "Accountant"),
        ("Marketer", "Marketer"),
        ("Cashier", "Cashier"),
        ("Driver", "Driver"),
        ("Customer care", "Customer care")
    
    ]

user_status = [
        ("", ""),
        ("Active", "Active"),
        ("Retired", "Retired"),
        ("Suspended", "Suspended"),
        ("Freeze", "Freeze"),
        ("On Leave", "On Leave"),
    ]



# class SignUpForm(UserCreationForm):
#     pass

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Profile_form(forms.ModelForm):
    profile_passport = forms.ImageField(required=False, help_text="Optional")
    particulars = forms.ImageField(required=False, help_text="Optional")
    position = forms.ChoiceField(required=False, choices=position, help_text="Optional")
    staff = forms.BooleanField(required=False, help_text="Optional")
    user_status = forms.ChoiceField(required=False, choices=user_status, help_text="Optional")


    # sex = forms.ChoiceField(required=True, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        exclude = [
            "profile",
            "user",
            "position",
            

        ]

        widgets = {
            "date_of_birth": forms.NumberInput(attrs={"type": "date"}),
            "sex": forms.RadioSelect(),
        }

class User_form(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            
        ]


class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_message
        fields = ['name', 'email', 'subject', 'message',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 5}),
        }

