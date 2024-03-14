from django.urls import path
from . import views
from portfolio_app.views import *
from .views import portfolioUpdate

urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    #views.index is the function defined in views.py def index(request)
    #name='indexx' parameters is to dynamically create url
    # example in html (a href="{% url 'index' %}">Home</a>)
    path('', views.index, name='index'),
    path("students/", StudentListView.as_view(), name='students'),
    path("student/<int:pk>", StudentDetailView.as_view(), name='student-detail'),
    path("portfolio/<int:pk>", PortfolioDetailView.as_view(), name="portfolio-detail"),
    path("portfolio/<int:portfolio_id>/project_form", views.createProject, name='project_form'),
    path("portfolio/<int:portfolio_id>/portfolio_form", views.portfolioUpdate, name='portfolio_update'),
    path("portfolio/<int:project_id>/project_update", views.projectUpdate, name='project_update'),
]
