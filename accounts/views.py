from collections import UserDict
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import UserForm, ProfileForm, UserCreatForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreatForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login/')

    else:
        form = UserCreatForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)

    context = {'profile': profile}

    return render(request, 'accounts/profile.html', context)


def view_profile(request, pk=None):
    profile = get_object_or_404(Profile)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user,
            'profile': profile,

            }
    return render(request, 'profile.html', args)


def om_oss(request):
    return render(request, 'om_oss.html')



