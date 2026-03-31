import pygame,random
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
pacman2=pygame.sprite.Group()
enemies=pygame.sprite.Group()

pacman3=pacman()
pacman2.add(pacman3)

for i in range(5):
    enemy_add=enemy()
    enemy_add.rect.x=random.randint(0,1000)
    enemy_add.rect.y=random.randint(0,500)
    
    enemies.add(enemy_add)
    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pacman2.draw(screen)
    enemies.draw(screen)
    pygame.display.update()