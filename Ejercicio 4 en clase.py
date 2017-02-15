import pygame,random
from pygame.locals import *

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
    rojo = (200, 0, 0)
    verde = (0, 255, 0)
    delta = 18 # tamaño de particula 

    clock=pygame.time.Clock()

    particulas = []
    for part in range(70):  #Cantidad de partículas     
        particulas.append( Particle(delta * random.randint(0, xmaxima//delta), delta * random.randint(0, ymaxima//delta)) ) #Ajuste de posicion inicial

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(fondo)
        posicion = []
        for p in particulas:
            p.move(delta, xmaxima, ymaxima)
            ubicacion = (p.x, p.y)# formato de ubicacion 
            color = rojo
            if ubicacion not in posicion:
                posicion.append(ubicacion)
            else:
                color = verde 
            pygame.draw.circle(screen, color, (p.x, p.y), delta // 2 - 2)

        pygame.display.flip()
        clock.tick(5) #Ajuste del tiempo
    pygame.quit()

if __name__ == "__main__":
    main()
