import math
import re
import pandas as pd
import numpy as np
import itertools
import time
from string import ascii_uppercase


def main():

    fileName = "Day21.txt"
    #fileName = "Day21example.txt"
    #read in file
    f = open(fileName,'r')
    #START = time.perf_counter_ns()

    alergens = {}
    ingredients = []
    food = []
    for line in f:
        food.append(line.strip(')\n').split(" (contains "))
    f.close()
    
    for f in food:
        l = f[0].split(' ')
        ingredients = ingredients + l
        for a in f[1].split(', '):
            if a in alergens:
                alergens[a] = alergens[a].intersection(set(l))
            else:
                alergens[a] = set(l)
                
    oneForEach = False
    while not oneForEach:
        for k in alergens:
            if len(alergens[k]) == 1:
                ingredient = list(alergens[k])[0]
                for key in alergens:
                    if k != key:
                        if ingredient in alergens[key]:
                            alergens[key].remove(ingredient)
        oneForEach = True
        for k in alergens:
            if len(alergens[k]) > 1:
                oneForEach = False
                break

    alergyIngredients = {"blank"}
    for k in alergens:
        alergyIngredients = alergyIngredients.union(alergens[k])
    alergyIngredients.remove("blank")

    nonAllergyIngredients = alergyIngredients.symmetric_difference(
        set(ingredients))

    result = 0
    for n in nonAllergyIngredients:
        result += ingredients.count(n)
        
    alphaKeys = sorted(alergens.keys())
    badBoys = ""
    for k in alphaKeys:
        ingr = list(alergens[k])[0]
        badBoys = badBoys + "," + ingr
        print(ingr, "   \thas\t", k)
    
    print("Non Allergy Ingredient Count = ", result)
    print("Canonical Dangerous Ingredient List:", badBoys[1:len(badBoys)])
    #END = time.perf_counter_ns()
    #print(f"Part 1 took {END-START} nanoseconds.")

main()
