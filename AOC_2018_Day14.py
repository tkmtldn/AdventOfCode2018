a = '635041'
recipes = '37'
e1 = 0
e2 = 1
while a not in recipes[-7:]:
    recipes += str(int(recipes[e1]) + int(recipes[e2]))
    e1 = (e1 + 1 + int(recipes[e1]))%len(recipes)
    e2 = (e2 + 1 + int(recipes[e2]))%len(recipes)
print(recipes[int(a):int(a)+10])
print(recipes.index(a))
