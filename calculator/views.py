from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, recipe_name):
    # Проверяем, существует ли такой рецепт
    if recipe_name not in DATA:
        raise Http404("Такого рецепта не знаю :(")

    # Получаем рецепт
    recipe = DATA[recipe_name].copy()

    # Получаем количество порций из GET-запроса, по умолчанию 1
    servings_str = request.GET.get('servings', '1')
    try:
        servings = int(servings_str)
        if servings <= 0:
            servings = 1
    except (ValueError, TypeError):
        servings = 1

    # Умножаем количество ингредиентов на количество порций
    for ingredient, amount in recipe.items():
        recipe[ingredient] = amount * servings

    # Формируем контекст для шаблона
    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)