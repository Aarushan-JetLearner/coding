import pgzrun,random
import pgzrun,time
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
    screen.draw.filled_rect(Welcome,"green")
    screen.draw.filled_rect(Question,"blue")
    screen.draw.filled_rect(Timer,"red")
    screen.draw.filled_rect(Skip,"green")
    screen.draw.filled_rect(Option1,"green")
    screen.draw.filled_rect(Option2,"green")
    screen.draw.filled_rect(Option3,"green")
    screen.draw.filled_rect(Option4,"green")
    screen.draw.textbox("Welcome to Quiz Master!",Welcome,color="white",shadow=(0.5,0.5),scolor="grey")
    screen.draw.textbox(str(timer),Timer, color="white", shadow=(0.5,0.5),scolor="black")
    screen.draw.textbox("Skip",Skip,color="white",shadow=(0.5,0.5),scolor="grey")
    screen.draw.textbox(q[0],Question,color="white")
    screen.draw.textbox(q[1],Option1,color="white")
    screen.draw.textbox(q[2],Option2,color="white")
    screen.draw.textbox(q[3],Option3,color="white")
    screen.draw.textbox(q[4],Option4,color="white")

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
    
file_data=["What year did the Titanic sink?,1911,1912,1913,1914,2","Which country has the most islands in the world?,Japan,Sweden,Finland,Norway,4","Who was the first President of the United States?,George Washington,John Adams,Thomas Jefferson,James Madison,1","What is the longest river in the world?,Nile,Yangtze,Amazon River,Yellow River,1","What is the capital city of Canada?Toronto,Ottawa,Vancouver,Montreal,2","Which ancient civilization built the pyramids?,Egyptian,Aegean,Iranian,Assyria,1","Who discovered penicillin?,Ernst Boris Chain,Howard Florey,Alexander Fleming,Leon Trotsky,3","What is the smallest country in the world?,Monaco,Vatican City,Nauru,Tuvalu,2","In which year did World War II end?,1945,1944,1946,1947,1","What is the tallest mountain in the world?Everest,K2,Kanchenjunga,Lhotse,1"]

def read_qu():
    random.shuffle(file_data)
    print(file_data)
    return file_data.pop(0).split(",")
def on_mouse_down(pos):
    index=1
    global score
    for i in option_boxes:
        if i.collidepoint(pos):
            if index is int[q[5]]:
                score=score+1
        index=index+1
q=read_qu()
clock.schedule_interval(changing_time,1)
pgzrun.go()