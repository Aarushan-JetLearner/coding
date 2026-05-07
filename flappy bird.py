import pygame,random
pygame.init()
screen=pygame.display.set_mode((1000,500))
bg=pygame.image.load("C:/Users/User/OneDrive/Pro game developer/bg.png")
bg=pygame.transform.scale(bg,(1000,500))
ground=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\ground.png")
ground=pygame.transform.scale(ground,(1000,50))
screen.blit(bg,(0,0))
pipes=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\pipe.png")
screen.blit(pipes,(0,0))
groundx=0
game_over=False
flying=False
pipe_frequency=2000

last_pipe=pygame.time.get_ticks()-pipe_frequency
pipe_gap=150
pass_pipe=False
score=0
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.count=0
        self.index=0
        self.vel=0
        self.clicked=False

        self.images=[]
        image=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird1.png")
        image2=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird2.png")
        image3=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\bird3.png")
        self.images.append(image)
        self.images.append(image2)
        self.images.append(image3)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=x,y
    def update(self):
        
        if flying==True:

            self.vel=self.vel+0.5
            if self.vel>=10:
                self.vel=10
            if self.rect.bottom<=450:
                self.rect.y=self.rect.y+self.vel

        self.count=self.count+1
        self.store=5
        if self.count>=self.store:
            self.count=0
            self.index=self.index+1
            if self.index>2:
                self.index=0
        self.image=self.images[self.index]
        if game_over==False:
            if self.clicked==False and pygame.mouse.get_pressed()[0]==1:
                print("Left button pressed")
                self.clicked=True
                self.vel=-10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
                #self.vel=10
class pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,top_bottom):
        super().__init__()
        self.image=pygame.image.load(r"C:\Users\User\OneDrive\Pro game developer\pipe.png") 
        self.rect=self.image.get_rect()
        if top_bottom==0:#down
            self.image=pygame.transform.rotate(self.image,180)
            self.rect.bottomleft=[x,y-(pipe_gap/2)]
        if top_bottom==1:#up
            self.rect.topleft=[x,y+(pipe_gap/2)]
    def update(self):
        
        self.rect.x=self.rect.x-10
        if self.rect.x<0:
            self.kill()
        

bird_group=pygame.sprite.Group()
pipe_group=pygame.sprite.Group()

bird_object=bird(250,250)
bird_group.add(bird_object)

def draw_text(score,font):
    scores=font.render("Score="+score,False,"white")
    screen.blit(scores,(50,50))


font=pygame.font.SysFont("Arial",35)
clock=pygame.time.Clock()
while game_over==False:

    clock.tick(60)
    screen.blit(bg,(0,0))
    draw_text(str(score),font)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True
    screen.blit(ground,(groundx,450))
    if game_over==False:
        time_get=pygame.time.get_ticks()
        
        if time_get-last_pipe>pipe_frequency:
            random_distance=random.randint(-150,150)
            pipe_object=pipes(1000,250-random_distance,0)
            pipe_object2=pipes(1000,250-random_distance,1)
            pipe_group.add(pipe_object)
            
            pipe_group.add(pipe_object2)
            last_pipe=time_get
        
        pipe_group.update()        
        if pipe_group:
            if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right<pipe_group.sprites()[0].rect.right and pass_pipe==False:
                pass_pipe=True
            if pass_pipe==True:
                if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.right:
                    score=score+1
                    pass_pipe=False
            elif pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or bird_object.rect.top<0:
                game_over=True
                    
                    #scores=font.render("Score="+str(score),False,"white")

                    
        
        

    
        groundx=groundx-1
    
        if abs(groundx)>20:
           groundx=0
    
        
    if bird_object.rect.bottom>=450:
        game_over=True
        flying=False

    bird_group.draw(screen)
    pipe_group.draw(screen)
    
    bird_object.update()
    
    #pipe_object.update()
    pygame.display.update()