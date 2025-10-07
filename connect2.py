import pgzrun,random
WIDTH=1000
HEIGHT=500
actors=[]
for i in range(8):
    actor=Actor("dot (1)")
    actor.x=random.randint(1,850)
    actor.y=random.randint(1,450)
    actors.append(actor)
def draw():
    screen.blit("bg white (1)",(0,0))
    number=1
    for i in actors:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]))
        number=number+1
pgzrun.go()