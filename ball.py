import pgzrun
WIDTH=1000
HEIGHT=1000
class ball():
    def __init__(self,color,x,y,radius):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
    def drawcircle(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
Object=ball("white",0,0,15)
def draw():

    Object.drawcircle()



pgzrun.go()