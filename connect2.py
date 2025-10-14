import pgzrun,random
from time import time
WIDTH=1000
HEIGHT=500
actors=[]
lines=[]
totalactors=8
actor1=0
startingtime=0
endingtime=0
totaltime=0
for i in range(8):
    actor=Actor("dot (1)")
    actor.x=random.randint(1,850)
    actor.y=random.randint(1,450)
    actors.append(actor)
startingtime=time()
print(startingtime)   
def draw():
    global totaltime
    screen.blit("bg white (1)",(0,0))
    screen.blit("r2",(0,0))
    number=1
    for i in actors:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]))
        number=number+1
    for i in lines:
        screen.draw.line(i[0],i[1],"black")
    if actor1<totalactors:
        totaltime=time()-startingtime
        screen.draw.text(str(totaltime),(20,20),fontsize=25)
    else:
        screen.draw.text(str(totaltime),(20,20),fontsize=25)
def update():
    pass
def on_mouse_down(pos):
    global lines, actor1
    if actor1<totalactors:
        if actors[actor1].collidepoint(pos):
            if actor1:
                lines.append((actors[actor1-1].pos,actors[actor1].pos))
            actor1=actor1+1
        else:
            lines=[]
            actor1=0
pgzrun.go()