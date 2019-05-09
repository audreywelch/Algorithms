#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  
  # Property to hold the number of batches that can be made
  batches = float("inf")

  # O(n)
  # Loop through each key in recipe
  for key in recipe.keys():

    # If the key exists in the ingredients available...
    if key in ingredients:

      # Value in recipe is less than or equal to the value in ingredients
      if recipe[key] <= ingredients[key]:

        # Divide the number of ingredients by the number needed for recipe
        # to get the number of batches
        current_batches = int(math.floor(ingredients[key] // recipe[key]))

        # Replace the number of batches with the smaller number because
        # we can only make as many batches as our lowest ingredient
        if current_batches < batches:
          batches = current_batches

      # Value in recipe is more than the value in ingredients
      else:
        batches = 0

    # Otherwise, if the key doesn't exist in the ingredients available, return 0
    else:
      batches = 0

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'flour': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))