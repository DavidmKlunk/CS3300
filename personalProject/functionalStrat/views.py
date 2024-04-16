from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

def index(request):
    expansions = Expansion.objects.all()
    return render(request, 'functionalStrat/index.html', {'expansions':expansions})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='raid_member')
            user.groups.add(group)
            member = RaidMember.objects.create(user=user,)
            member.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context ={'form':form}
    return render(request, 'registration/register.html', context)


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

@login_required(login_url='login')
@allowed_users(allowed_roles=['raid_leader'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['raid_leader', 'raid_assistant'])
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

