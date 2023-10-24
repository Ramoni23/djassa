from django.db import models

# Create your models here.

# creation de la category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# creation des articles
class Article(models.Model):
    title= models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc= models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title