from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import *

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
    

    