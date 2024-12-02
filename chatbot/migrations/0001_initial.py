# Generated by Django 5.1.3 on 2024-12-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bilan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatbotResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger_phrase', models.CharField(max_length=100)),
                ('response_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_facture', models.CharField(max_length=100, unique=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_emission', models.DateField()),
                ('statut', models.CharField(choices=[('payée', 'Payée'), ('impayée', 'Impayée')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Firme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_firme', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
            ],
        ),
    ]