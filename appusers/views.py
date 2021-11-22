from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from django.views.generic import CreateView , TemplateView
from curriculum.models import Standard
from appusers.forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate , login ,logout



# Create your views here.
class HomeView(TemplateView):
    template_name = 'appusers/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standards = Standard.objects.all()
        teachers = Profile.objects.filter(user_type='teacher')
        context['standards'] = standards
        context['teachers'] = teachers
        return context

                                # registering a user
def register(request):
    registered = False  
    if request.method == 'POST':
        user_form  = UserForm(data = request.POST)
        profile_form  = ProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            registered =True

        else:
            print(user_form.errors , profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {'registered':registered , 'user_form':user_form , 'profile_form':profile_form}
    return render(request , 'appusers/register.html' ,context )

                            #  User Login

def user_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username = username , password = password)

        if user:
            if user.is_active:
                login(request , user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")

        else:
             return HttpResponse("Pleasee enter the correct Username and Password")

    else:
        return render(request , 'appusers/login.html')

                                    # User Logout

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'appusers/contact.html'