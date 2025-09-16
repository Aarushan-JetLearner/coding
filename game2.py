import pgzrun, random
WIDTH=1000
HEIGHT=1000
TITLE="Catch two moving characters game"
actor=Actor("mariop-removebg-preview")
actor2=Actor("sonic th")
message=("Hello")
def draw():
    screen.fill("blue")
    actor.draw()
    actor2.draw()
    screen.draw.text(message,center=(250,250),fontsize=25)   
def on_mouse_down(pos):
    global message
    if actor.collidepoint(pos):
        message=("Good shot!")
        actor.x=random.randint(0,500)
        actor.y=random.randint(0,500)
    else:
        message=("You missed")
    if actor2.collidepoint(pos):
        message=("Good shot")
        actor2.x=random.randint(0,500)
        actor2.y=random.randint(0,500)
    else:
        message=("You missed")

pgzrun.go()