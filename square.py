import pgzrun
WIDTH=500
HEIGHT=500

def draw():
    length=150
    width=150
    for i in range(6):
        rectangle=Rect((0,0),(length,width))
        rectangle.center=(250,250)
        screen.draw.rect(rectangle,"red")
        length=length-25
        width=width-25






pgzrun.go()