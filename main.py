def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()
            cook_book[dish_name] = ingredients
        print(cook_book)

    shoping_list_dishes = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredients in cook_book[dish]:
                key = ingredients['ingredient_name']
                if key in shoping_list_dishes.keys():
                    shoping_list_dishes[key]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    measure = ingredients['measure']
                    shoping_list_dishes[key] = {'quantity': int(ingredients['quantity']) * person_count, 'measure': measure}

    return shoping_list_dishes

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 3))
