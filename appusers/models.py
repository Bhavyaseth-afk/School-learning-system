from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import os

# Adding image directly to image folder when the user enters it

def path_and_rename(instance , filename):
    upload_to = 'images/'
    ext = filename.split(".")[-1]

    if instance.user.username:
        filename= 'UserProfilePic/{}.{}'.format(instance.user.username , ext)
    return os.path.join(upload_to , filename)

# creating user's class

class Profile(models.Model):
        user = models.OneToOneField(User , on_delete=models.CASCADE)
        bio = models.CharField(max_length= 150 , blank=True)
        profile_pic  = models.ImageField(upload_to = path_and_rename, verbose_name=
        'Profile Picture' , blank = True)


        teacher = 'teacher'
        student = 'student'
        parent = 'parent'

        user_types= [
            (teacher , 'teacher'),
            (student , 'student'),
            (parent , 'parent'),
        ]

        user_type = models.CharField(max_length=10 , choices=user_types , default= student) 

        def __str__(self):
            return self.user.username
        

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')