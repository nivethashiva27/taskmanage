from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h2>Task Manager API</h2>
        <p>Go to <a href="/api/tasks/">/api/tasks/</a></p>
        <p>Frontend: <a href="/frontend/">/frontend/</a></p>
    """)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('frontend/', include('tasks.frontend_urls')),  # frontend route (we create next)
]
