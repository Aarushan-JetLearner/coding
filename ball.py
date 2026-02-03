import pgzrun,os
os.environ["SDL_VIDEO_CENTERED"]="1"
WIDTH=1000
HEIGHT=1000
Gravity=2000
class ball():
    def __init__(self,color,x,y,radius):
        self.color=color
        self.x=x
        self.y=y
        self.radius=radius
        self.velocityx=200
        self.velocityy=0
    def drawcircle(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
Object=ball("red",30,0,30)
Object2=ball("white",970,0,30)
#Object2=ball("green",30,60,30)Object3=ball("blue",30,120,30)Object4=ball("red",30,180,30)
def draw():
    screen.clear()
    Object.drawcircle()
    Object2.drawcircle()
    #Object3.drawcircle()Object4.drawcircle()
def update(dt):

    initialvelocityy=Object.velocityy
    Object.velocityy=Object.velocityy+Gravity*dt
    Object.y=Object.y+(initialvelocityy+Object.velocityy)/2*dt
    if Object.y>1000:
        Object.velocityy=-Object.velocityy*0.85
    Object.x=Object.x+Object.velocityx*dt
    if Object.x>=1000 or Object.x<=0:
        Object.velocityx=-Object.velocityx
    initialvelocityy2=Object2.velocityy
    Object2.velocityy=Object2.velocityy+Gravity*dt
    Object2.y=Object2.y+(initialvelocityy2+Object2.velocityy)/2*dt
    if Object2.y>1000:
        Object2.velocityy=-Object2.velocityy*0.95
    Object2.x=Object2.x+Object2.velocityx*dt
    if Object2.x>=1000 or Object2.x<=0:
        Object2.velocityx=-Object2.velocityx



pgzrun.go()