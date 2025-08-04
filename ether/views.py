from django.shortcuts import render

# Create your views here.
def home(request):
    welcome = "Hello, Welcome to Mimi's epresso"
    return render(request, 'index.html', {"welcome": welcome})