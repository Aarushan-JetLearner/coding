import pygame
screen=pygame.display.set_mode((1000,500))
class pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/R__1_-removebg-preview (2) (1).png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()
pacman2=pygame.sprite.Group()
pacman3=pacman()
pacman2.add(pacman3)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pacman2.draw(screen)
    pygame.display.update()