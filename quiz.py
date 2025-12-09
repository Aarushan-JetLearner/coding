import pgzrun,time
WIDTH=1000
HEIGHT=500
Welcome=Rect(0,0,1000,60)
Question=Rect(5,75,800,150)
Timer=Rect(850,100,150,150)
Skip=Rect(850,275,150,200)
Option1=Rect(0,240,400,125)
Option2=Rect(425,240,400,125)
Option3=Rect(0,380,400,125)
Option4=Rect(425,380,400,125)
def draw():
    screen.fill(color="black")
    screen.draw.filled_rect(Welcome,"orange")
    screen.draw.filled_rect(Question,"blue")
    screen.draw.filled_rect(Timer,"blue")
    screen.draw.filled_rect(Skip,"green")
    screen.draw.filled_rect(Option1,"orange")
    screen.draw.filled_rect(Option2,"orange")
    screen.draw.filled_rect(Option3,"orange")
    screen.draw.filled_rect(Option4,"orange")
    screen.draw.textbox("Welcome to Quiz Master.",Welcome,color="white",shadow=(0.5,0.5),scolor="grey")
    screen.draw.textbox(str(timer),Timer,color="white",shadow=(0.5,0.5),scolor="black")
    screen.draw.textbox("Skip",Skip,color="white",angle=90,shadow=(0.5,0.5),scolor="blue")
def update():
    Welcome.x=Welcome.x-2
    if Welcome.right<0:
        Welcome.left=1000
    
    


timer=15
def changing_time():
    global timer
    
    if timer>0:
        timer=timer-1
    
    else:
        timer=0
clock.schedule_interval(changing_time,1)
file_data=[]


    

pgzrun.go()
