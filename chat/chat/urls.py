
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('chat_app.urls')),
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),
]
