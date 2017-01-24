Permitidos = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
from random import choice
N = []
for particulas in range(8):
	coord = [choice(Permitidos) for x in range(3)]
	N.append(coord)
print (N)
