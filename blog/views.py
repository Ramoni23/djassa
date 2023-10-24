from django.shortcuts import render
from .models import Article

# Create your views here.

# creation de la view page d'accueil
def home(request):
    # afficher le model article sur la page d'accueil
    list_articles = Article.objects.all()
    context = {"list_articles":list_articles}
    return render(request, "index.html", context)

# creation de la view detail
def detail(request, id_article):
    article =Article.objects.get(id=id_article)
    category = article.category # obtenir  toutes les category
    # obtenir les articles de la meme relation que le precedent
    article_en_relation = Article.objects.filter(category=category)[:5] # affiche les 5 premiers
    
    context = {"article":article, "article_en_relation":article_en_relation}
    return render(request, 'detail.html', context)