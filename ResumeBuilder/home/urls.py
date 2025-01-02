from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('ResumeBuilder/', views.ResumeBuilder, name='ResumeBuilder'),
    path('choose-template/', views.choose_template, name='choose_template'),
    path('fill-form/<int:template_id>/', views.fill_form, name='fill_form'),

     path('preview-resume/<int:resume_id>/', views.preview_resume, name='preview_resume'),
    path('download-resume/<int:resume_id>/', views.download_resume, name='download_resume'),

    

]
