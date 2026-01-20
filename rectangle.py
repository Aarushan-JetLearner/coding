import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Rectangle")
screen.fill("blue")
pygame.display.update()
class Rect():
    def __init__(self,color,dimension):
        self.dimension=dimension
        self.color=color
    def draw(self):
        pygame.draw.rect(screen,self.color,self.dimension)
Object=Rect("white",(0,0,100,50))
Object.draw()
Object2=Rect("black",(150,150,100,50))
Object2.draw()
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


