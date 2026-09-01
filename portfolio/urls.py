from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_home, name='home'),
    path('experience/', views.experience_view, name='experience'),
    path('education/', views.education_view, name='education'),
    path('projects/', views.projects_view, name='projects'),
    path('skills/', views.skills_view, name='skills'),
    path('certifications/', views.certifications_view, name='certifications'),
    path('extracurriculars/', views.extracurriculars_view, name='extracurriculars'),
    path('references/', views.references_view, name='references'),
]