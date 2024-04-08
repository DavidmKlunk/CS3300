from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    expansions = Expansion.objects.all()
    return render(request, 'functionalStrat/index.html', {'expansions':expansions})

class BossStratDetailView(DetailView):
    model = BossStrat

class BossStratListView(ListView):
    model = BossStrat

class ExpansionListView(ListView):
    model = Expansion

class ExpansionDetailView(DetailView):
    model = Expansion

class RaidListView(ListView):
    model = Raid

class BossDetailView(DetailView):
    model = Boss

class RaidDetailView(DetailView):
    model = Raid
def createStrat(request, boss_id):
    form = StratForm()
    boss = Boss.objects.get(pk=boss_id)
    
    if request.method == 'POST':
        strat_data = request.POST.copy()
        strat_data['boss_id'] = boss_id
        form = StratForm(strat_data)

        if 'Cancel' in request.POST:
            return redirect('boss-detail',boss_id)
        
        elif form.is_valid():
            strat = form.save(commit=False)
            strat.boss = boss
            strat.save()

            return redirect('boss-detail',boss_id)
    context = {'form': form}
    return render(request, 'functionalStrat/update_create_form.html', context)    

def updateStrat(request, strat_id):
    strat = BossStrat.objects.get(pk=strat_id)
    form = StratForm(instance=strat)

    if request.method == 'POST':
        form = StratForm(request.POST, instance=strat)

        if 'Cancel' in request.POST:
            return redirect('boss-detail', strat.boss.pk)
        
        elif form.is_valid():
            form.save()
            return redirect('strat-detail', strat_id)
        
    context = {'form': form}
    return render(request, 'functionalStrat/update_create_form.html', context)

def deleteStrat(request, strat_id):
    strat = BossStrat.objects.get(pk=strat_id)

    if request.method == 'POST':

        if 'Cancel' in request.POST:
            return redirect('boss-detail', strat.boss.pk)
        
        else:
            strat.delete()
            return redirect('boss-detail', strat.boss.pk)
    
    return render(request,'functionalStrat/delete_form.html', {'strat': strat})

