import pygame
pygame.init()
screen=pygame.display.set_mode((1000,500))
bg=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/bg.png")
bg=pygame.transform.scale(bg,(1000,500))
ground=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\ground.png")
ground=pygame.transform.scale(ground,(1000,50))
screen.blit(bg,(0,0))
groundx=0
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images=[]
        image=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird1.png")
        image2=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird2.png")
        image3=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird3.png")
        self.images.append(image)
        self.images.append(image2)
        self.images.append(image3)
        self.image=self.images[0]
        self.rect=self.image.get_rect()
bird_group=pygame.sprite.Group()
bird_object=bird(250,250)
bird_group.add(bird_object)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    groundx=groundx-1
    screen.blit(ground,(groundx,450))
    if abs(groundx)>20:
        groundx=0
    bird_group.draw(screen)

    pygame.display.update()