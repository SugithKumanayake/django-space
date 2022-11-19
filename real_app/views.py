from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request,'real_app/index.html')
def about_page(request):
    return render(request,'real_app/about.html')
def contact_page(request):
    return render(request,'real_app/contact.html')
def services_page(request):
    return render(request,'real_app/services.html')
def team_page(request):
    return render(request,'real_app/team.html')