import pygame,random
from pygame.locals import *

xmaxima = 750    
ymaxima = 700     


class Particle():
    def __init__(self, iniciox, inicioy, color):
        self.x = iniciox
        self.y = inicioy
        self.color = color
        self.sx = iniciox
        self.sy = inicioy

    def move(self):
        if self.y < 0:
            self.x=self.sx
            self.y=self.sy

        else:
            self.y-=random.randint(-2, 2)

        self.x+=random.randint(-2, 2) 

def main():  
    pygame.init()
    screen = pygame.display.set_mode((xmaxima,ymaxima))
    white = (255, 255, 255) 
    black = (0,0,0)
    grey = (128,128,128)

    clock=pygame.time.Clock()

    particulas = []
    for part in range(350):
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        particulas.append( Particle(random.randint(0, xmaxima), random.randint(0,ymaxima), color) )

    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True
                    
        screen.fill(white)
        for p in particulas:
            p.move()
            pygame.draw.circle(screen, p.color, (p.x, p.y), 3)
            
        pygame.display.flip()
        clock.tick(50) 
    pygame.quit()

if __name__ == "__main__":
    main()


    
