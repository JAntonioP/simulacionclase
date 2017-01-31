import random
histograma= []
from matplotlib.pylab import hist, show
Permitidos = 80
from random import choice
N = []
for particulas in range(150):
	coord = [random.randrange (0, 150, 2) for x in range(3)]
	N.append(coord)
print (N)
from math import sqrt
for particulas in N:
	dist= sqrt(sum([x**2 for x in particulas]))
	print (dist)
	histograma.append(dist)
	
hist (histograma,100, (0,300))
show()
