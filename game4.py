import pgzrun,random
WIDTH=700
HEIGHT=600
TITLE="catch pikachu"
actor=Actor("oip (1)")
actor2=Actor("ash2")
score=0
actor.pos=100,100

actor2.pos=100,500
def draw():
    screen.blit("bg (2)",(0,0))
    actor.draw()
    actor2.draw()
    screen.draw.text("score="+str(score),color="black",fontsize=25,topleft=(50,50))
def update():
    global score
    if keyboard.left:
        actor2.x=actor2.x-10
    if keyboard.right:
        actor2.x=actor2.x+10
    if keyboard.up:
        actor2.y=actor2.y-10
    if keyboard.down:
        actor2.y=actor2.y+10
    if actor2.colliderect(actor):
        actor.x=random.randint(0,600)
        actor.y=random.randint(0,600)
        score=score+10



pgzrun.go()