from random import randint, choice
n=20
tiempo=100
posicion=randint (0, n)
for paso in range (tiempo):
	print ('-'*(posicion - 1) + '°' + '-'*(n - posicion))
	posicion += choice ([1, -1])

if posicion > n:
	posicion -= n
elif posicion < 0:
        posicion  += n
