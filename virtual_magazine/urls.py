from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('home.urls', namespace='home')),
    path('polls/', include('polls.urls', namespace='polls')),
    path('auth/', include('authentication.urls', namespace='authentication')),
    #path('admin/', admin.site.urls),
]
