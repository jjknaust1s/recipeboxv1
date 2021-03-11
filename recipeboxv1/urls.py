"""recipeboxv1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homepage import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('recipes/<int:post_id>/', views.recipe_detail, name='recipe_detail'),
    path('addrecipe/', views.add_recipe, name='add_recipe'),
    path('addauthor/', views.add_author, name='add_author'),
    path('editrecipe/<int:recipe_id>/', views.edit_view, name='editrecipe'),
    path('favorite/<int:recipe_id>/', views.favorite_view, name='favorite'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
