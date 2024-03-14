from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import *
from .forms import ProjectForm, PortfolioForm, StudentForm
from django.views.generic.edit import UpdateView

# Create your views here.

def index(request):
    ##return HttpResponse('home page')
    #return render( request, 'portfolio_app/index.html')
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class PortfolioDetailView(DetailView):
    model = Portfolio

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()

            return redirect('portfolio-detail', portfolio_id)
        
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def projectUpdate(request, project_id):
    form = ProjectForm()
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['project_id'] = project_id
        form = ProjectForm(project_data)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = project.portfolio
            project.save()

            return redirect('portfolio-detail', project.portfolio)
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


def portfolioUpdate(request, portfolio_id):
    form = PortfolioForm
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        portfolio_data = request.POST.copy()
        portfolio_data['portfolio_id'] = portfolio_id
        form = PortfolioForm(portfolio_data)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.save()

            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/portfolio_form.html', context)
    