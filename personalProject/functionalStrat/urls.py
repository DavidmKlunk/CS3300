from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('strat/<int:strat_id>/update_project', views.updateStrat, name='update-strat'),
    path('strat/<int:strat_id>/delete_strat', views.deleteStrat, name='delete-strat'),
    path('boss/<int:boss_id>/add_strat', views.createStrat, name='create-strat'),
    path('boss/<int:pk>', views.BossDetailView.as_view(), name='boss-detail'),
    path('strat/<int:pk>', views.BossStratDetailView.as_view(), name='strat-detail'),
    path('expansion/<int:pk>',views.ExpansionDetailView.as_view(), name='expansion-detail'),
    path('raid/<int:pk>',views.RaidDetailView.as_view(),name='raid-detail'),
    
]
