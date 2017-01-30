histograma= []
from matplotlib.pylab import hist, show
Permitidos = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
from random import choice
N = []
for particulas in range(8):
	coord = [choice(Permitidos) for x in range(3)]
	N.append(coord)
print (N)
from math import sqrt
for particulas in N:
	dist= sqrt(sum([x**2 for x in particulas]))
	print (dist)
	histograma.append(dist)
	
hist (histograma,8, (0,60))
show()
