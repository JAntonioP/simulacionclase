import pygame,random
from pygame.locals import *
from math import sqrt

xmaxima = 500    #ancho de la pantalla
ymaxima = 500     #alto de la pantalla

class Particle():
    def __init__(self, iniciox, inicioy):
        self.x = iniciox
        self.y = inicioy
        self.sx = iniciox
        self.sy = inicioy

    def move(self, d, mx, my): # tipo de movimiento 
        cambio = d
        if random.random() < 0.5: # condiciones de movimiento (en dona).
            cambio *= -1
        if random.random() < 0.5:
            self.y += cambio
            if self.y < 0:
                self.y += my
            elif self.y > my:
                self.y -= my
        else:
            self.x += cambio
            if self.x < 0:
                self.x += mx
            elif self.x > mx:
                self.x -= mx
        

def main():  #declaracion de colores
    pygame.init()
    screen = pygame.display.set_mode((xmaxima,ymaxima))
    fondo = (255, 255, 255) 

    clock=pygame.time.Clock()

    particulas = []
    tam = []# lista de tamaño de particula 
    delta = 50 # paso
    cuantos = 20 # numero de particulas
    tope = 70 # tope maximo para que cambie su color 
    for part in range(cuantos):  #Cantidad de partículas     
        particulas.append( Particle(delta * random.randint(0, xmaxima//delta), delta * random.randint(0, ymaxima//delta)) ) #Ajuste de posicion inicial
        tam.append(random.randint(1, 30)) # tamaño aleatorio de la particula 
        #tam.append (10) # tamaño fijo de la particula 

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(fondo)
        colision = set()# conjunto de coliciones 
        for pi in range(cuantos):# particula inicial 
            p = particulas[pi] # p son particulas iniciales 
            p.move(delta, xmaxima, ymaxima)

        for pi in range(cuantos - 1): # 2 tipos de particulas iniciales p1 y p2 
            p1 = particulas[pi]
            for pj in range(pi + 1, cuantos):
                p2 = particulas[pj]# comparacion de una particula con otra segun la distancia que tengan 
                dist = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)# la distancia es igual a la raiz cuadrada de las posiciones p1 y p2 
                if dist < tam[pi] + tam[pj]: # declaracion de coliciones dependiendo de la magnitud del tamaño de las particulas 
                   colision.add(pi)
                   colision.add(pj)
            
        for pos in range(cuantos):# posicion de particula dependiendo de la cantidad de particulas 
            p = particulas[pos]
            if pos in colision:
                tam[pos] *= 1.02 # porsentaje de crecimiento dependiendo de la posicion de la particula
                if tam[pos] > tope:
                    tam[pos] = tope # declaracion de crecimiento maximo de las particulas 
            aux = int(round(tam[pos]))
            pygame.draw.circle(screen, (p.x % 255, p.y % 255, min(aux, 255)), (p.x, p.y), aux)# cambio de color deacuerdo al tamaño de la particula 

        pygame.display.flip()
        clock.tick(5) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
