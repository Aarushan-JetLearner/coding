import pygame
pygame.init()
screen=pygame.display.set_mode((1000,500))
space=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/39625.jpg")
space=pygame.transform.scale(space,(1000,500))
spaceship_width=55
spaceship_height=55
font=pygame.font.SysFont("Arial",35)
yellow_spaceship=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/R__1_-removebg-preview.png")
yellow_spaceship=pygame.transform.scale(yellow_spaceship,(spaceship_width,spaceship_height))
yellow_spaceship=pygame.transform.rotate(yellow_spaceship,-90)
yellow_spaceship_health=10
red_spaceship=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/redr-removebg-preview.png")
red_spaceship=pygame.transform.scale(red_spaceship,(spaceship_width,spaceship_height))
red_spaceship=pygame.transform.rotate(red_spaceship,90)
red_spaceship_health=10
mid_rect=pygame.Rect(500,0,10,500)
def drawing(Rect,Rect2,yellow_spaceship_health,red_spaceship_health):
    screen.blit(space,(0,0))
    screen.blit(red_spaceship,(Rect.x,Rect.y))
    screen.blit(yellow_spaceship,(Rect2.x,Rect2.y))
    pygame.draw.rect(screen,"black",mid_rect)
    yellow_text=font.render("Health="+str(yellow_spaceship_health),False,"white")
    screen.blit(yellow_text,(250,50))
    red_text=font.render("Health="+str(red_spaceship_health),False,"white")
    screen.blit(red_text,(750,50))
    pygame.display.update()

Rect=pygame.Rect(750,250,spaceship_width,spaceship_height)
Rect2=pygame.Rect(250,250,spaceship_width,spaceship_height)
while True:
    drawing(Rect,Rect2,yellow_spaceship_health,red_spaceship_health)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and Rect.x>500:
                Rect.x=Rect.x-10
            elif event.key==pygame.K_RIGHT and Rect.x+spaceship_width<1000:
                Rect.x=Rect.x+10
            elif event.key==pygame.K_UP and Rect.y>0:
                Rect.y=Rect.y-10
            elif event.key==pygame.K_DOWN and Rect.y+spaceship_height<500:
                Rect.y=Rect.y+10

    
