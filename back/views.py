from django.shortcuts import render
from accounts.models import CustomUser
from back.models import Subject, Formation
from django.contrib.auth import get_user_model

User = get_user_model()

def Dashboard(request):
    template_name = 'back/dashboard.html'
    context = {}
    return render(request, template_name, context)


def Users(request):
    users = User.objects.all().order_by('id')
    template_name = 'back/users.html'
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def Formations(request):
    subjects = Subject.objects.all().order_by('id')
    formations = Formation.objects.all().order_by('id')
    template_name = 'back/formations.html'
    context = {
        'subjects': subjects,
        'formations': formations,
    }
    return render(request, template_name, context)
