import pygame
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
object_non_recylable=plastic_bag()
non_recylable.add(object_non_recylable)
all_sprites.add(object_non_recylable)
all_sprites.add(object_bin)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    all_sprites.draw(screen)
    pygame.display.update()
