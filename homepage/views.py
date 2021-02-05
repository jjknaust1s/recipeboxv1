from django.shortcuts import render

from homepage.models import Author, Recipe

# Create your views here.

def index(request):
    recipe = Recipe.objects.all()
    return render(request, 'index.html',{'recipe': recipe})

def recipe_detail(request, post_id):
    detail = Recipe.objects.get(id=post_id)
    recipe = Recipe.objects.filter(id=post_id)
    return render(request, 'recipe_detail.html', {
        'detail':detail,
        'recipe': recipe
        })

def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author_obj)
    return render(request, 'author_detail.html', {
        'author':author_obj,
        'recipes':recipes
        })
    