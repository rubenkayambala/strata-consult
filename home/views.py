from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from back.models import Subject, Formation, Domaine, Emploi


def Home(request):
    template_name = 'home/index.html'
    return render(request, template_name)

def Etude_sol(request):
    template_name = 'home/etude_sol.html'
    return render(request, template_name)


def EmploiList(request):
    domaines = Domaine.objects.all()
    emplois = Emploi.objects.all().order_by('-id')
    template_name = 'home/emploi.html'
    context = {
        'domaines': domaines,
        'emplois': emplois,
    }
    return render(request, template_name, context)

def DetailEmploi(request, pk):
    emploi = get_object_or_404(Emploi, pk=pk)
    domaines = Domaine.objects.all()
    template_name = 'home/detail_emploi.html'
    context = {
        'emploi': emploi,
        'domaines': domaines,
    }
    return render(request, template_name, context)


def Appel(request):
    template_name = 'home/appel.html'
    return render(request, template_name)

def Immobilier(request):
    template_name = 'home/immobilier.html'
    return render(request, template_name)

def Achat(request):
    template_name = 'home/achat.html'
    return render(request, template_name)


def FormationList(request):
    formations = Formation.objects.all().order_by('-date')
    template_name = 'home/formation.html'
    context = {
        'formations': formations,
    }
    return render(request, template_name, context)

def DetailFormation(request, slug):
    formation = get_object_or_404(Formation, slug=slug)
    template_name = 'home/detail_formation.html'
    context = {
        'formation': formation,
    }
    return render(request, template_name, context)


def FollowFormation(request, slug):
    user = request.user
    souscrire = False
    if request.method == 'POST':
        formation = Formation.objects.get(slug=slug)
        if user not in formation.souscrire.all():
            formation.souscrire.add(user)
            souscrire = True
            context = {
                'formation': formation,
                'souscrire': souscrire,
                'souscrire_number': formation.souscrire.count(),
                }
            return HttpResponseRedirect(reverse('home:detail_formation', args=[slug]))
    else:
        return render(request, 'home/formation.html')
    return render(request, template_name, context)

def UnfollowFormation(request, slug):
    user = request.user
    souscrire = True
    if request.method == 'POST':
        formation = Formation.objects.get(slug=slug)
        if user in formation.souscrire.all():
            formation.souscrire.remove(user)
            souscrire = False
            context = {
                'formation': formation,
                'souscrire': souscrire,
                'souscrire_number': formation.souscrire.count(),
                }
            return HttpResponseRedirect(reverse('home:detail_formation', args=[slug]))
    else:
        return render(request, 'home/formation.html')


def Contact(request):
    template_name = 'home/contact.html'
    return render(request, template_name)
    
