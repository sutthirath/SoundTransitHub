from django.shortcuts import render

# Function based views

def index(request):
    return render(request, 'index.html')
