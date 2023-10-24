from django.contrib import admin
from .models import Article, Category

# Register your models here.
# enregistrer le model Article dans admin
admin.site.register(Article)
# enregistrer le model Category dans admin
admin.site.register(Category)

