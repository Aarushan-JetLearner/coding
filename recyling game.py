import pygame,random
pygame.init()
screen=pygame.display.set_mode((1000,500))
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/bin rec game.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
class plastic_bag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/plastic rec game.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
recylable=pygame.sprite.Group()
non_recylable=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()

object_bin=bin()
for i in range(20):
    object_non_recylable=plastic_bag()
    object_non_recylable.rect.x=random.randint(0,1000)
    object_non_recylable.rect.y=random.randint(0,500)
    non_recylable.add(object_non_recylable)
    all_sprites.add(object_non_recylable)
all_sprites.add(object_bin)
list=["C:/Users/User/OneDrive/Pro game developer/item1 rec game.png","C:/Users/User/OneDrive/Pro game developer/item2 rec game.png","C:/Users/User/OneDrive/Pro game developer/item3 rec game.png"]
class rec(pygame.sprite.Sprite):
    def __init__(self,imagea):
        super().__init__()
        self.image=pygame.image.load(imagea)
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
for i in range(30):
    object_recylable=rec(random.choice(list))
    object_recylable.rect.x=random.randint(0,1000)
    object_recylable.rect.y=random.randint(0,500)
    recylable.add(object_recylable)
    all_sprites.add(object_recylable)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and object_bin.rect.x>0:
                object_bin.rect.x=object_bin.rect.x-10
            
            if event.key==pygame.K_RIGHT and object_bin.rect.x<1000:
                object_bin.rect.x=object_bin.rect.x+10

            if event.key==pygame.K_UP and object_bin.rect.y>0:
                object_bin.rect.y=object_bin.rect.y-10
         
            if event.key==pygame.K_DOWN and object_bin.rect.y<1000:
                object_bin.rect.y=object_bin.rect.y+10
            
    screen.fill("black")
    all_sprites.draw(screen)
    pygame.display.update()
