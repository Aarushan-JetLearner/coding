import pygame
pygame.init()
screen=pygame.display.set_mode((1000,500))
space=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/39625.jpg")
space=pygame.transform.scale(space,(1000,500))
spaceship_width=55
spaceship_height=55
yellow_spaceship=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/R (1).jpg")
yellow_spaceship=pygame.transform.scale(yellow_spaceship,(spaceship_width,spaceship_height))
red_spaceship=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/redr.jpg")
red_spaceship=pygame.transform.scale(red_spaceship,(spaceship_width,spaceship_height))
mid_rect=pygame.Rect(500,0,10,500)
def drawing():
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",mid_rect)
    pygame.display.update()


while True:
    drawing()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    
