from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        needs = {rec: set(ing) for rec, ing in zip(recipes, ingredients)}

        updated = True

        while updated:
            updated = False

            for rec in recipes:
                if rec in available:
                    continue

                if needs[rec].issubset(available):
                    available.add(rec)
                    updated = True

        return [rec for rec in recipes if rec in available]