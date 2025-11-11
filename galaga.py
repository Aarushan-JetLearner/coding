import pgzrun
WIDTH=1000
HEIGHT=500
actor1=Actor("galaga")
actor2=Actor("bug")
actor1.pos=(500,450)
def draw():
    screen.fill("black")
    actor1.draw()
    actor2.draw()
    

pgzrun.go()