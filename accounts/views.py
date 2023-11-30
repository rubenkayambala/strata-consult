from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from back.models import Formation, Emploi
from django.contrib.auth import get_user_model


User = get_user_model()


def Register(request):
    template_name = 'accounts/register.html'
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Données incorrectes! Réessayez")
            form = UserUpdateForm()
            context = {
                'form': form,
            }
            return render(request, template_name, context)
    form = UserUpdateForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def Login(request):
    username_email = request.POST.get('username_email')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(username=username_email).exists()):
            user = authenticate(username=username_email, password=password)
        elif(User.objects.filter(email=username_email).exists()):
            user = User.objects.get(email=username_email)
            user = authenticate(username=user.username, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('home:home')
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "Mot de passe incorrects! Réessayez")
            return redirect('home:home')
    else:
        return render(request, 'home/index.html')


def Logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def Profile(request, username):
    user = get_object_or_404(User, username=username)
    context = { 
        'user': user,
        }
    return render(request, 'accounts/profile.html', context)


@login_required
def UpdateProfile(request, pk):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile', args=[pk]))
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})
    

@login_required
def MesFormations(request):
    current_user = request.user
    return render(request, 'accounts/formations.html')
    