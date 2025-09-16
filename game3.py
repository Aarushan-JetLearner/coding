import pgzrun,random
WIDTH=1000
HEIGHT=1000
TITLE="flying bee"
actor=Actor("flower")
actor2=Actor("bee")
score=0

actor.pos=100,100

actor2.pos=100,0
def draw():
    
    screen.blit("sky (1)",(0,0))
    actor.draw()
    actor2.draw()
    screen.draw.text("score="+str(score),color="black",fontsize=25,topleft=(50,50))
def update():
    global score
    if keyboard.left:
        actor2.x=actor2.x-10
    if keyboard.right:
        actor2.x=actor2.x+10
    if keyboard.down:
        actor2.y=actor2.y+10
    if keyboard.up:
        actor2.y=actor2.y-10
    if actor2.colliderect(actor):
        actor.x=random.randint(0,1000)
        actor.y=random.randint(0,1000)
        score=score+10
pgzrun.go()
