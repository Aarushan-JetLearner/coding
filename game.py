import pgzrun,random
WIDTH=500
HEIGHT=500
TITLE="alien game"
actor=Actor("alien-removebg-preview (1)")
message=("Hello!")
def draw():
    screen.fill("red")
    actor.draw()
    screen.draw.text(message,center=(250,250),fontsize=25)   
def on_mouse_down(pos):
    global message
    if actor.collidepoint(pos):
        message=("Good shot!")
        actor.x=random.randint(0,500)
        actor.y=random.randint(0,500)
    else:
        message=("You missed")
    

pgzrun.go()