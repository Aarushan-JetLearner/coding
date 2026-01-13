import pgzrun,time,random
WIDTH=1000
HEIGHT=500
score=0
Welcome=Rect(0,0,1000,60)
Question=Rect(5,75,800,150)
Timer=Rect(850,100,150,150)
Skip=Rect(850,275,150,200)
Option1=Rect(0,240,400,125)
Option2=Rect(425,240,400,125)
Option3=Rect(0,380,400,125)
Option4=Rect(425,380,400,125)
option_boxes=[Option1,Option2,Option3,Option4]
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
    screen.draw.textbox(qu[0],Question,color="white")
    screen.draw.textbox(qu[1],Option1,color="white")
    screen.draw.textbox(qu[2],Option2,color="white")
    screen.draw.textbox(qu[3],Option3,color="white")
    screen.draw.textbox(qu[4],Option4,color="white")
    
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

        
file_data=["What is the capital of Sri Lanka?, Colombo, Jaffna, California, London,1","What is the only U.S. state that can be typed using only one row of a standard QWERTY keyboard?,California,Alaska,Texas,New York,2", "Which ear did Vincent Van Gogh cut off?,Left ear,right ear,neither,both,1", "What is the only mammal that can fly?,Aardvark,Baboon,Camel,Bat,4" ,"What was the first toy advertised on TV?,Barbie dolls,Lego sets,Mr. Potato Head,G.I. Joe,3", "What is the capital of France?,Marseille,Paris,Nice,Lyon,2"]

def read_q():
    random.shuffle(file_data)
    print(file_data)
    return file_data.pop(0).split(",")
def on_mouse_down(pos):
    global score
    message="Game over Score"+str(score)
    index=1
    global qu
    global timer
    if Skip.collidepoint(pos):
        if len(file_data)>0:
            qu=read_q()
            timer=15
        else:
            qu=[message,"-","-","-","-",5]
            timer=0
    for i in option_boxes:

        if i.collidepoint(pos):
            if index ==int(qu[5]):
                score=score+1
                print(score)
                if len(file_data)>0:
                    qu=read_q()
                    timer=15
                else:
                    qu=[message,"-","-","-","-",5]
                    timer=0
        index=index+1
qu=read_q()

clock.schedule_interval(changing_time,1) 

pgzrun.go()
