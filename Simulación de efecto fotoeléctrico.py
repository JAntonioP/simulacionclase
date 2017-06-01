import pygame
from pygame.locals import *
import random, math, sys
pygame.init()

Pantalla = pygame.display.set_mode((800,600))
Barras = []
Circles = []
nc = 8
ne = 10
t = 0
f = 0
listo = False

class Circle:
    def __init__(self, fijo=False, x=None):
##        self.radius = int(random.random()*50) + 1
        self.radius = 10
        self.libre = True
        if not fijo:
            self.x = random.randint(self.radius, 800-self.radius)
            self.y = random.randint(self.radius, 500-self.radius)
            self.speedx = 0.1*(random.random()+1.0)
            self.speedy = 0.1*(random.random()+1.0)
            self.electron = False
        else:
            self.speedx = 0
            self.speedy = 0
            self.y = 550
            self.x = x
            self.electron = True
##        self.mass = math.sqrt(self.radius)

for x in range(nc):
    Circles.append(Circle())

div = 800 // (ne + 1)
for valor in range(1, ne + 1):
    Circles.append(Circle(True, valor * div)) 

def CircleCollide(C1, C2):
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x - C2.x)
    YDiff = -(C1.y - C2.y)
    de = sqrt(XDiff**2 + YDiff**2)
    if de < 20:
        Angle = 0
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
        if fabs(XDiff) > 0.00001:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed * math.cos(math.radians(Angle))
            YSpeed = -C1Speed * math.sin(math.radians(Angle))
        if not C1.electron:    
            C1.speedx = XSpeed
            C1.speedy = YSpeed
        else:
            C1.speedx = 0
            C1.speedy = -0.2
        if not C2.electron:
            C2.speedx = -XSpeed
            C2.speedy = -YSpeed
        else:
            C2.speedx = 0
            C2.speedy = -0.2

from math import fabs, sqrt

def Move():
    global f, listo
    for Circle in Circles:
        if not Circle.libre:
            continue
        Circle.x += Circle.speedx
        Circle.y -= Circle.speedy
        if Circle.x < 10: # izq
            Circle.x = -Circle.x
            Circle.speedx = -Circle.speedx
        elif Circle.x > 790: # der
            Circle.x = 2 * 800 - Circle.x
            Circle.speedx = -Circle.speedx
        if Circle.y > 540: # abajo
            Circle.y = 2 * 550 - Circle.y
            Circle.speedy = -Circle.speedy
        elif Circle.y < 60: # arriba
            Circle.y = 2 * 50 - Circle.y
            if not Circle.electron:
                Circle.speedy = -Circle.speedy
            else: # se fija un electron
                Circle.speedy = 0
                Circle.libre = False
                Circle.y = 60
                f += 1
                print(t, f)
                if f == ne:
                    listo = True
        
def CollisionDetect():
    k = len(Circles)
    for i in range(k - 1):
        Circle = Circles[i]
        if Circle.electron and Circle.y < 550:
            continue
        for j in range(i + 1, k):
            Circle2 = Circles[j]
            if Circle2.electron and Circle.y < 550:
                continue
            if not Circle.electron or not Circle2.electron:
                CircleCollide(Circle, Circle2)

def Draw():
    Pantalla.fill((236,234,229))
    for Circle in Circles:
        if not Circle.electron: 
            pygame.draw.circle(Pantalla, (16,85,152),     (int(Circle.x),int(Circle.y)),10)
            pygame.draw.circle(Pantalla, (255, 255, 255), (int(Circle.x),int(Circle.y)), 5)
        else:
            pygame.draw.circle(Pantalla, (150,150,150),     (int(Circle.x),int(Circle.y)),10)
    pygame.draw.rect(Pantalla,(200, 0, 0),(0,0,800,50)) # arriba
    pygame.draw.rect(Pantalla,(200, 0, 0),(0,550,800,50)) # abajo
    pygame.display.flip()

def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():    
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()

def main():
    global t
    while not listo:
        GetInput()
        Move()
        CollisionDetect()
        Draw()
        t += 1
    pygame.quit(); sys.exit()
    
if __name__ == '__main__': main()
