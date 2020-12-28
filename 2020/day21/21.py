def collect_data():
    data = []
    with open("./21.input") as file:
        for line in file:
            data.append(line.strip())
    return data


def find_potential_allergen_food(data):
    cnt = {}
    for line in data:
        food, allergens = line.strip(")").split(" (contains ")
        for allergen in allergens.split(", "):
            if allergen not in cnt:
                cnt[allergen] = set(food.split())
            else:
                cnt[allergen] &= set(food.split())
    return cnt


def get_all_foods(data):
    foods = []
    for line in data:
        food, allergens = line.split(" (")
        foods.extend(food.split())
    return foods


def find_allergen_food(potential_foods):
    confirmed = {}
    # If there is only one food (value) for the allergen (key), then that
    # food's allergen is confirmed. Repeat this until all foods have only
    # one allergen
    while len(confirmed) != len(potential_foods):
        for food, allergen in potential_foods.items():
            if len(allergen) == 1:
                confirmed[food] = allergen.pop()
            for k, v in potential_foods.items():
                potential_foods[k] -= set(confirmed.values())
    return confirmed


def runner():
    data = collect_data()

    all_foods = get_all_foods(data)
    potential_allergen_foods = find_potential_allergen_food(data)
    allergen_foods = find_allergen_food(potential_allergen_foods)

    part1 = sum(1 for f in all_foods if f not in allergen_foods.values())
    part2 = [allergen_foods[f] for f in sorted(allergen_foods)]

    print("Part 1:", part1)
    print("Part 2:", ','.join(part2))


if __name__ == '__main__':
    runner()
