from django.db import models

# Modèle pour représenter un bilan
class Bilan(models.Model):
    date = models.DateField()  # Date du bilan
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant du bilan
    description = models.TextField(blank=True, null=True)  # Description optionnelle

    def __str__(self):
        return f"Bilan du {self.date} - {self.montant} Ar"

# Modèle pour représenter une facture
class Facture(models.Model):
    numero_facture = models.CharField(max_length=100, unique=True)  # Numéro unique de la facture
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant de la facture
    date_emission = models.DateField()  # Date d'émission de la facture
    statut = models.CharField(max_length=50, choices=[('payée', 'Payée'), ('impayée', 'Impayée')])  # Statut de la facture

    def __str__(self):
        return f"Facture {self.numero_facture} - {self.montant} Ar"

# Modèle pour représenter une firme
class Firme(models.Model):
    nom_firme = models.CharField(max_length=200)  # Nom de la firme
    adresse = models.CharField(max_length=500)  # Adresse de la firme
    email = models.EmailField()  # Email de contact
    telephone = models.CharField(max_length=15)  # Numéro de téléphone de la firme

    def __str__(self):
        return self.nom_firme

class ChatbotResponse(models.Model):
    trigger_phrase = models.CharField(max_length=100)  # Phrase déclencheur (ex : "Bonjour")
    response_text = models.CharField(max_length=255)   # Réponse à afficher (ex : "Bonjour, comment ça va ?")

    def __str__(self):
        return self.trigger_phrase
