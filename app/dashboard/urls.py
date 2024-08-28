from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('background/', views.background, name='background'),
    path('glossary/', views.glossary, name='glossary'),
    path('download/', views.download, name='download'),
    path('documentation/', views.documentation, name='documentation'),
    path('quickfacts/', views.quickfacts, name='quick facts'),
    # re_path('^.*$', views.catch_all, name='catch_all'),
]
