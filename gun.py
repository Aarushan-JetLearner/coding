import pygame
pygame.init()
screen=pygame.display.set_mode((1000,500))
gunbg=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/pngtree-fighting-championship-night-captivating-side-scene-view-of-mma-octagon-under-image_13532945.png")
gunbg=pygame.transform.scale(gunbg,(1000,500))
gun_width=55
gun_height=55
font=pygame.font.SysFont("Arial",35)
red_gun=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/OIP__7_-removebg-preview.png")
red_gun=pygame.transform.scale(red_gun,(gun_width,gun_height))
red_gun=pygame.transform.rotate(red_gun,0)
red_gun_health=10
blue_gun=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/96-965653_gun-clip-art-blue-gun-clip-art-removebg-preview (1).png")
blue_gun=pygame.transform.scale(blue_gun,(gun_width,gun_height))
blue_gun=pygame.transform.rotate(blue_gun,0)
blue_gun_health=10
mid_rect=pygame.Rect(495,0,5,500)
mid_rect2=pygame.Rect(500,0,5,500)
def drawing(Rect,Rect2,red_gun_health,blue_gun_health):
    screen.blit(gunbg,(0,0))
    screen.blit(blue_gun,(Rect.x,Rect.y))
    screen.blit(red_gun,(Rect2.x,Rect2.y))
    pygame.draw.rect(screen,"red",mid_rect)
    pygame.draw.rect(screen,"blue",mid_rect2)
    pygame.display.update()
Rect=pygame.Rect(750,250,gun_width,gun_height)
Rect2=pygame.Rect(250,250,gun_width,gun_height)
while True:
    drawing(Rect,Rect2,red_gun_health,blue_gun_health)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and Rect.x>500:
                Rect.x=Rect.x-10
            elif event.key==pygame.K_RIGHT and Rect.x+gun_width<1000:
                Rect.x=Rect.x+10
            elif event.key==pygame.K_UP and Rect.y>0:
                Rect.y=Rect.y-10
            elif event.key==pygame.K_DOWN and Rect.y+gun_height<500:
                Rect.y=Rect.y+10
            if event.key==pygame.K_a and Rect2.x>0:
                Rect2.x=Rect2.x-10
            elif event.key==pygame.K_d and Rect2.x+gun_width<495:
                Rect2.x=Rect2.x+10
            elif event.key==pygame.K_w and Rect2.y>0:
                Rect2.y=Rect2.y-10
            elif event.key==pygame.K_s and Rect2.y+gun_height<500:
                Rect2.y=Rect2.y+10

                