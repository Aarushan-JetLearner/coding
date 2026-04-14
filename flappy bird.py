import pygame
pygame.init()
screen=pygame.display.set_mode((1000,500))
bg=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/bg.png")
bg=pygame.transform.scale(bg,(1000,500))
ground=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\ground.png")
ground=pygame.transform.scale(ground,(1000,50))
screen.blit(bg,(0,0))
groundx=0
game_over=False
flying=False
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.count=0
        self.index=0
        self.vel=0
        self.clicked=False

        self.images=[]
        image=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird1.png")
        image2=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird2.png")
        image3=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird3.png")
        self.images.append(image)
        self.images.append(image2)
        self.images.append(image3)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self):
        if flying==True:

            self.vel=self.vel+5
            if self.vel>=10:
                self.vel=10
            if self.rect.bottom<=450:
                self.rect.y=self.rect.y+self.vel

        self.count=self.count+1
        self.store=5
        if self.count>=self.store:
            self.count=0
            self.index=self.index+1
            if self.index>2:
                self.index=0
        self.image=self.images[self.index]
        


bird_group=pygame.sprite.Group()
bird_object=bird(250,250)
bird_group.add(bird_object)


while True:
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True
    screen.blit(ground,(groundx,450))
    if game_over==False:
        groundx=groundx-1
        if abs(groundx)>20:
           groundx=0
        
    if bird_object.rect.bottom>=450:
        game_over=True
        flying=False

    bird_group.draw(screen)
    
    
    bird_object.update()

    pygame.display.update()