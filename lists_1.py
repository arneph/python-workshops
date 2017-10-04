movies = ['Interstellar', 'Star Trek', 'Contact']
favorite = movies[2]
movies[1] = 'Star Wars'
movies.extend(['2001: A Space Odyssey', 'Alien'])
movies.insert(3, 'The Martian')
movies.remove('Interstellar')
movies.pop()
i = movies.index('Star Wars')
l = len(movies)
movies.sort()
movies.reverse()

print(movies)
print(favorite)
print(i)
print(l)