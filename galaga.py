import pgzrun,random
WIDTH=1000
HEIGHT=500
actor1=Actor("galaga")
actor2=Actor("bug")
actor1.pos=(500,450)
def draw():
    screen.fill("black")
    actor1.draw()
    for i in bullets:
        i.draw()
    for i in enemies:
        i.draw()
def update():
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
    for i in enemies:
        if i.y<=500:
            i.y=i.y+5
        else:
            i.y=-50
            i.x=random.randint(50,950)

        
     
    
bullets=[]
def on_key_down(key):
    if key==keys.SPACE:
      bullets.append(Actor("bullet"))
      bullets[-1].x=actor1.x
      bullets[-1].y=actor1.y-50

enemies=[]
enemies.append(actor2)
enemies[-1].x=500
enemies[-1].y=0




        
        


pgzrun.go()