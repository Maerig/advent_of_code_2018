PUZZLE_INPUT = 360781


def get_recipes():
    recipes = [3, 7]
    first_index, second_index = 0, 1
    while True:
        first_recipe = recipes[first_index]
        second_recipe = recipes[second_index]
        recipe_sum = first_recipe + second_recipe
        first_new_recipe = recipe_sum // 10
        if first_new_recipe:
            recipes.append(first_new_recipe)
            yield recipes
        recipes.append(recipe_sum % 10)
        yield recipes
        first_index = (first_index + first_recipe + 1) % len(recipes)
        second_index = (second_index + second_recipe + 1) % len(recipes)


def part_1(recipe_goal):
    recipes_gen = get_recipes()
    recipes = []
    while len(recipes) < recipe_goal + 10:
        recipes = next(recipes_gen)
    return ''.join(str(recipe) for recipe in recipes[-10:])


def part_2(recipe_goal):
    recipe_goal_arr = [
        int(recipe)
        for recipe in str(recipe_goal)
    ]
    recipe_goal_length = len(recipe_goal_arr)
    recipes_gen = get_recipes()
    recipes = []
    while recipes[-recipe_goal_length:] != recipe_goal_arr:
        recipes = next(recipes_gen)
    return len(recipes) - len(recipe_goal_arr)


if __name__ == '__main__':
    print(f"Part 1: {part_1(PUZZLE_INPUT)}")
    print(f"Part 2: {part_2(PUZZLE_INPUT)}")
