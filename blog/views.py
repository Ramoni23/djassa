from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    # afficher le model article sur la page d'accueil
    list_articles = Article.objects.all()
    context = {"list_articles":list_articles}
    return render(request, "index.html", context)