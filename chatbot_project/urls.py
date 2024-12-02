from django.contrib import admin
from chatbot import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('chatbot/', include('chatbot.urls')),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]
