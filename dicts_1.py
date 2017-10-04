ratings = {'Titanic':4, '500 Days of Summer':3, 'Twilight':1}
stars = ratings['500 Days of Summer']
ratings['La La Land'] = 3
del ratings['Twilight']

print(ratings)
print(stars)