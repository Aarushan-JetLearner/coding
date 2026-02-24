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
def drawing(Rect,Rect2,yellow_spaceship_health,red_spaceship_health,bullet_yellow):
    screen.blit(space,(0,0))
    screen.blit(red_spaceship,(Rect.x,Rect.y))
    screen.blit(yellow_spaceship,(Rect2.x,Rect2.y))
    pygame.draw.rect(screen,"black",mid_rect)
    yellow_text=font.render("Health="+str(yellow_spaceship_health),False,"white")
    screen.blit(yellow_text,(250,50))
    red_text=font.render("Health="+str(red_spaceship_health),False,"white")
    screen.blit(red_text,(750,50))
    for i in bullet_yellow:
        pygame.draw.rect(screen,"yellow",i)
    for i in bullet_red:
        pygame.draw.rect(screen,"red",i)
    pygame.display.update()
def move_bullets(bullet_red,bullet_yellow,Rect,Rect2):
    for i in bullet_red:
        i.x=i.x-10
        if Rect2.colliderect(i):
            bullet_red.remove(i)
        elif i.x<0:
            bullet_red.remove(i)

    for i in bullet_yellow:
        i.x=i.x+10
        if Rect.colliderect(i):
            bullet_yellow.remove(i)
        elif i.x>1000:
            bullet_yellow.remove(i)

    
bullet_red=[]
bullet_yellow=[]
Rect=pygame.Rect(750,250,spaceship_width,spaceship_height)
Rect2=pygame.Rect(250,250,spaceship_width,spaceship_height)
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    drawing(Rect,Rect2,yellow_spaceship_health,red_spaceship_health,bullet_yellow)
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
            elif event.key==pygame.K_a and Rect2.x>0:
                Rect2.x=Rect2.x-10
            elif event.key==pygame.K_d and Rect2.x+spaceship_width<500:
                Rect2.x=Rect2.x+10
            elif event.key==pygame.K_w and Rect2.y>0:
                Rect2.y=Rect2.y-10
            elif event.key==pygame.K_s and Rect2.y+spaceship_height<500:
                Rect2.y=Rect2.y+10
            elif event.key==pygame.K_LCTRL and len(bullet_yellow)<3:
                bullet=pygame.Rect(Rect2.x+spaceship_width,Rect2.y+spaceship_height/2,2,3)
                bullet_yellow.append(bullet)
            elif event.key==pygame.K_RCTRL and len(bullet_red)<3:
                bullet2=pygame.Rect(Rect.x,Rect.y+spaceship_height/2,10,3)
                bullet_red.append(bullet2)
            move_bullets(bullet_red,bullet_yellow,Rect,Rect2)



    
