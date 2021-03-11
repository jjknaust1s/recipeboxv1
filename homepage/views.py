from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from homepage.models import Author, Recipe
from homepage.forms import AddRecipeForm, AddAuthorForm, SignupForm, LoginForm


# Create your views here.
def index(request):
    recipe = Recipe.objects.all()
    return render(request, 'index.html', {'recipe': recipe})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data["username"],
                                password=data['password'])
            if user:
                login(request, user)

            return HttpResponseRedirect(request.GET.get('next',
                                                        reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('homepage'))


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
    fav = author_obj.favorites.all()
    return render(request, 'author_detail.html', {
        'author': author_obj,
        'recipes': recipes,
        'fav': fav
        })


@login_required
def add_recipe(request):
    context = {}
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe.objects.create(
                title=data['title'],
                author=request.user.author,
                description=data['description'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse(
                                        'recipe_detail', args=[new_recipe.id]))

    form = AddRecipeForm()
    context.update({'form': form})
    return render(request, 'generic_form.html', context)


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                author=request.user.author,
                byline=data['byline']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, 'add_author.html', {'form': form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password']

            )
            Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=new_user
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required
def edit_view(request, recipe_id):
    editable_recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            editable_recipe.title=data.get('title')
            editable_recipe.description=data.get('description')
            editable_recipe.instructions=data.get('instructions')
            editable_recipe.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm(initial={'title': editable_recipe.title, 'description': editable_recipe.description, 'instructions': editable_recipe.instructions})
    return render(
        request,
        'generic_form.html',
        {'form': form}
    )


def favorite_view(request, recipe_id):
    user = Author.objects.get(user=request.user)
    fav_recipe = Recipe.objects.get(id=recipe_id)
    user.favorites.add(fav_recipe)
    user.save()
    print(user.favorites.all())
    return HttpResponseRedirect(reverse('homepage'))