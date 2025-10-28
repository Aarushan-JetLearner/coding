import pgzrun,random
WIDTH=1000
HEIGHT=1000
items=["bag","chips","battery","bottle","paper","bground"]
items_list=[]
animation=[]
game_over=False
game_complete=False
number_of_levels=7
initial_speed=10
current_level=1
def draw():
    screen.blit("bground",(0,0))
    if game_over:
        screen.draw.text("Game over!",fontsize=60,center=(500,100),color="white")
    elif game_complete:
        screen.draw.text("You've completed the game! Well done!",fontsize=60,center=(500,100),color="white")
    else:
        for i in items_list:
            i.draw()
def update():
    global items_list
    if len(items_list)==0:
        items_list=update_level(current_level)
     

def update_level(current_level):
    item2=["paper"]
    for i in range(current_level):
        variable=random.choice(items)
        item2.append(variable)

    
pgzrun.go()