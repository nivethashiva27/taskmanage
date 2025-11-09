from django.shortcuts import render

def tasks_frontend(request):
    return render(request, 'tasks/frontend.html')
