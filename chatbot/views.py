from django.shortcuts import render
from .models import Bilan, Facture, Firme
from .forms import ChatForm
from .models import ChatbotResponse
from django.http import JsonResponse

def chatbot_response(request):
    user_message = request.GET.get('message', '')
    response = ""

    if 'bonjour' in user_message.lower():
        response = "Bonjour! Comment puis-je vous aider aujourd'hui?"
    elif 'au revoir' in user_message.lower():
        response = "Au revoir! À bientôt!"
    else:
        response = "Je ne suis pas sûr de comprendre, pouvez-vous reformuler votre question?"

    return JsonResponse({'response': response})




def home(request):
    return render(request, 'home.html')

def bilan_view(request):
    bilans = Bilan.objects.all()
    return render(request, 'chatbot/bilan.html', {'bilans': bilans})

def facture_view(request):
    factures = Facture.objects.all()
    return render(request, 'chatbot/facture.html', {'factures': factures})

def firme_view(request):
    firmes = Firme.objects.all()
    return render(request, 'chatbot/firme.html', {'firmes': firmes})

def chat_view(request):
    response = ''
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            # Logique de réponse du chatbot (vous pouvez personnaliser cela)
            if 'bonjour' in user_message.lower():
                response = "Bonjour! Comment puis-je vous aider aujourd'hui?"
            else:
                response = "Désolé, je n'ai pas compris. Pouvez-vous reformuler?"
    else:
        form = ChatForm()

    return render(request, 'chatbot/chat.html', {'form': form, 'response': response})

def chatbot_view(request):
    user_input = request.GET.get('message', '')  # Obtenir le message de l'utilisateur
    response = "Désolé, je n'ai pas compris."  # Réponse par défaut

    # Chercher si le message de l'utilisateur correspond à un déclencheur
    if user_input:
        chatbot_responses = ChatbotResponse.objects.filter(trigger_phrase__icontains=user_input)
        if chatbot_responses:
            response = chatbot_responses.first().response_text

    return render(request, 'chatbot/chat.html', {'response': response, 'user_input': user_input})


