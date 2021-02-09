from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Author, Recipe
from homepage.forms import AddRecipeForm, AddAuthorForm


# Create your views here.
def index(request):
    recipe = Recipe.objects.all()
    return render(request, 'index.html', {'recipe': recipe})


def recipe_detail(request, post_id):
    detail = Recipe.objects.get(id=post_id)
    recipe = Recipe.objects.filter(id=post_id)
    return render(request, 'recipe_detail.html', {
        'detail': detail,
        'recipe': recipe
        })


def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author_obj)
    return render(request, 'author_detail.html', {
        'author': author_obj,
        'recipes': recipes
        })


def add_recipe(request):
    context = {}
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse(
                                        'recipe_detail', args=[new_recipe.id]))

    form = AddRecipeForm()
    context.update({'form': form})
    return render(request, 'generic_form.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})
