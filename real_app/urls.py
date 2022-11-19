from django.urls import path
from . import views

app_name = 'real_app'

urlpatterns = [
    path('',views.index_page,name='home'),
    path('about',views.about_page,name='about'),
    path('contact',views.contact_page,name='contact'),
    path('services',views.services_page,name='services'),
    path('team',views.team_page,name='team'),
]