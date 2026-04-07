import pygame,random
pygame.init()
screen=pygame.display.set_mode((1000,500))
class pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/R__1_-removebg-preview (2) (1).png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/R__2_-removebg-preview (1) (1).png")
        self.rect=self.image.get_rect()
class bg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/black background.jpg")
        self.rect=self.image.get_rect()
class collectibles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/yellow cicle.jpg")
        self.image=pygame.transform.scale(self.image,(25,25))
        self.rect=self.image.get_rect()
pacman2=pygame.sprite.Group()
enemies=pygame.sprite.Group()
background=pygame.sprite.Group()
collectibles_g=pygame.sprite.Group()
background2=bg()
background.add(background2)
pacman3=pacman()
pacman2.add(pacman3)


for i in range(5):
    enemy_add=enemy()
    enemy_add.rect.x=random.randint(0,1000)
    enemy_add.rect.y=random.randint(0,500)
    enemies.add(enemy_add)
    collectible_add=collectibles()
    collectible_add.rect.x=random.randint(0,1000)
    collectible_add.rect.y=random.randint(0,500)
    collectibles_g.add(collectible_add)
score=0    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and pacman3.rect.x>0:
                pacman3.rect.x=pacman3.rect.x-10
            
            if event.key==pygame.K_RIGHT and pacman3.rect.x<1000:
                pacman3.rect.x=pacman3.rect.x+10

            if event.key==pygame.K_UP and pacman3.rect.y>0:
                pacman3.rect.y=pacman3.rect.y-10
         
            if event.key==pygame.K_DOWN and pacman3.rect.y<500:
                pacman3.rect.y=pacman3.rect.y+10

    background.draw(screen)
    pacman2.draw(screen)
    enemies.draw(screen)
    collectibles_g.draw(screen)
    variable=pygame.sprite.spritecollide(pacman3,enemies,True)
    variable2=pygame.sprite.spritecollide(pacman3,collectibles_g,True)
    font=pygame.font.SysFont("Arial",50)
  
    for i in variable:
        score=score-1
    score_surface=font.render("Score="+str(score),False,"white")
    screen.blit(score_surface,(50,50))
    for i in variable2:
        score=score+1
    

    pygame.display.update()