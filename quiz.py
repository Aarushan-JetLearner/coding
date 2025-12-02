import pgzrun
WIDTH=1000
HEIGHT=500
Welcome=Rect(0,0,800,60)
Question=Rect(5,75,500,150)
def draw():
    screen.draw.filled_rect(Welcome,"orange")
    screen.draw.filled_rect(Question,"blue")

pgzrun.go()
