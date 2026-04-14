import pygame,random
pygame.init()
screen=pygame.display.set_mode((1000,500))
bg=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bgfalling fruit.webp")
bg=pygame.transform.scale(bg,(1000,500))
screen.blit(bg,(0,0))
class basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\basket.png")
        self.image=pygame.transform.scale(self.image,(75,75))
        self.rect=self.image.get_rect()
class fruits(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images=[]
        apple=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\pngtree-apple-fruit-cartoon-png-image_14611130.png")
        apple=pygame.transform.scale(apple,(50,50))
        grape=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\grape.jpg")
        grape=pygame.transform.scale(grape,(50,50))
        banana=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\pngtree-summer-fruit-cartoon-banana-png-image_3979229.jpg")
        banana=pygame.transform.scale(banana,(50,50))
        mango=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\mango.jpg")
        mango=pygame.transform.scale(mango,(50,50))
        orange=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\orange.jpg")
        orange=pygame.transform.scale(orange,(50,50))
        self.images.append(apple)
        self.images.append(grape)
        self.images.append(banana)
        self.images.append(mango)
        self.images.append(orange)
        self.image=self.images[0]
        self.rect=self.image.get_rect()
        
group_basket=pygame.sprite.Group()
group_fruits=pygame.sprite.Group()
object_basket=basket()
group_basket.add(object_basket)
group_basket.draw(screen)

object_fruits=fruits()
group_fruits.add(object_fruits)


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:

            pygame.quit()
            
        group_basket.draw(screen)
        group_fruits.draw(screen)
        pygame.display.update()
        