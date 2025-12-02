import pgzrun,random
WIDTH=1000
HEIGHT=500
actor1=Actor("galaga")
enemiess=[]
direction=1
game_over=False
for i in range(8):
    actor2=Actor("bug")
    enemiess.append(actor2)
    enemiess[-1].x=100+90*i
    enemiess[-1].y=-50
actor1.pos=(500,450)
score=0
def draw():
    global game_over
    screen.clear()
    screen.fill("black")
    actor1.draw()
    for i in bullets:
        i.draw()
    for i in enemiess:
        i.draw()
    screen.draw.text(str(score),(0,0))
    if game_over==True:
        screen.draw.text("Game over!",fontsize=60,center=(500,50))
def update():
    global direction
    move_down=False
    for i in enemiess:
        for j in bullets:
                global score
                if i.colliderect(j):
                    
                    bullets.remove(j)
                    enemiess.remove(i)
                    score=score+1
    if keyboard.left:
        if actor1.x>0:
            actor1.x=actor1.x-10
        else:
            actor1.x=actor1.x
    elif keyboard.right:
        if actor1.x<1000:
            actor1.x=actor1.x+10
        else:
            actor1.x=actor1.x
    elif keyboard.down:
        if actor1.y<500:
            actor1.y=actor1.y+10
        else:
            actor1.y=actor1.y
    elif keyboard.up:
        if actor1.y>0:
            actor1.y=actor1.y-10
        else:
            actor1.y=actor1.y
    for i in bullets:
        if i.y>0:
            i.y=i.y-15
        else:
            bullets.remove(i) 
    if enemiess and(enemiess[0].x<0 or enemiess[-1].x>1000):
        move_down=True
        direction=direction*-1
    if len(enemiess)==0:
        global game_over
        
        game_over=True

    for i in enemiess:
        i.x=i.x+5*direction
        if move_down==True:
            i.y=i.y+50

    
        
     
    
bullets=[]
def on_key_down(key):
    if key==keys.SPACE:
      bullets.append(Actor("bullet"))
      bullets[-1].x=actor1.x
      bullets[-1].y=actor1.y-50
      sounds.eep.play()






        
        


pgzrun.go()