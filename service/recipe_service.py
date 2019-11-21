import requests


class RecipeService:
    @staticmethod
    def get_recipe(ingredients):
        r = requests.get('http://www.recipepuppy.com/api/?i={}'.format(','.join(ingredients)))
        print(r.content)
