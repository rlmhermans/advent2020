with open('input') as f:
    fulltext = f.read()
    input = fulltext.splitlines()

candidates = {}
counts = {}
all_ingredients = set()

for line in input:
    ingredients, allergens = line.split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens[:-1].split(', '))
    
    for allergen in allergens:
        if allergen in candidates:
            candidates[allergen] &= ingredients
        else:
            candidates[allergen] = ingredients.copy()

    all_ingredients |= ingredients
    for ingredient in ingredients:
        counts[ingredient] = counts.get(ingredient, 0) + 1

allergens = [item for sublist in candidates.values() for item in sublist]
non_allergens = all_ingredients.difference(set(allergens))
occurences = [counts.get(non_allergen) for non_allergen in non_allergens]

print(sum(occurences))