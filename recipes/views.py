from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def all_recipes(request):
    """A view to allow the user to see the recipes available"""
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    """View to display details of a specific recipe"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    description_list = recipe.description.split('\n')
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'description_list': description_list})


@login_required
def add_recipe(request):
    """View to add a new recipe"""

    if not request.user.is_superuser:
        messages.error(request, 'Access not permitted.')
        return redirect(reverse('recipes'))

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe added successfully')
            return redirect('recipes')
        else:
            messages.error(request, 'An error occurred. Please check the form.')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


@login_required
def edit_recipe(request, recipe_id):
    """View to edit an existing recipe"""

    if not request.user.is_superuser:
        messages.error(request, 'Access not permitted.')
        return redirect('recipes')
    
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            return(redirect('recipes'))
        else:
            messages.error(request, 'Failed to update recipe. Please check the form.')
    else:
        form = RecipeForm(instance=recipe)
        messages.info(request, f'You are editing {recipe.brewing_type}')

    template = 'recipes/edit_recipe.html'
    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, template, context)


@login_required
def delete_recipe(request, recipe_id):
    """Delete a specific recipe"""
    if not request.user.is_superuser:
        messages.error(request, 'Access not permitted.')
        return redirect(reverse('home'))

    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe deleted!')
    return redirect('recipes')