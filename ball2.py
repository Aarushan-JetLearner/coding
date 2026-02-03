import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
class Circle():
    def __init__(self,color,x,y,radius):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
    def draw_circle(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    def draw_again(self,radius):
        self.radius=self.radius+radius
        self.draw_circle()

Object=Circle("white",30,30,15)

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            Object.draw_circle()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            Object.draw_again(15)
            pygame.display.update()