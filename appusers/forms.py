from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appusers.models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField()


    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')
        labels = {
            'password1' : 'Enter Pasaword' ,
            'password2': 'Confirm Pasaword'
        }


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(required = False)
    teacher = 'teacher'
    student = 'student'
    parent  = 'parent'


    
    user_types= [
        # (teacher , 'teacher'),NOT INCLUDING TEACHER BECASUE THE ADMIN WILL GIVE AUTHORITY TO THE TEACHER AND THEY WILL NOT BE ABLE TO REGISTER
        (student , 'student'),
        (parent , 'parent'),
        ]

    user_type = forms.ChoiceField(required = True, choices= user_types)

    class Meta():
        model = Profile
        fields = ('bio' , 'profile_pic' , 'user_type'  ) 



























































































































































