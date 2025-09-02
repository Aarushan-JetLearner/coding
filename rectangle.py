import pgzrun
WIDTH=500
HEIGHT=500
def draw():
    length=250
    width=200
    for i in range(5):
        rectangle=Rect((0,0),(length,width))
        rectangle.center=250,250
        screen.draw.rect(rectangle,"blue")
        length=length-25
        width=width-25
        
        

pgzrun.go()
