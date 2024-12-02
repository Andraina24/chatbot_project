from django.urls import path
from . import views

urlpatterns = [
    path('bilan/', views.bilan_view, name='bilan'),
    path('facture/', views.facture_view, name='facture'),
    path('firme/', views.firme_view, name='firme'),
    path('', views.chat_view, name='chat'),
    path('chat/', views.chatbot_response, name='chatbot_response'),

]
