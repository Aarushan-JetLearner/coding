import pgzrun,random
WIDTH=1000
HEIGHT=1000
items=["black","blue","white","red"]
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
        screen.draw.text("You lose!",fontsize=60,center=(500,100),color="white")
    elif game_complete:
        screen.draw.text("You win!",fontsize=60,center=(500,100),color="white")
    else:
        for i in items_list:
            i.draw()
def update():
    global items_list
    if len(items_list)==0:
        items_list=update_level(current_level)
def update_level(current_level):
    item2=["green"]
    for i in range(current_level):
        variable=random.choice(items)
        item2.append(variable)
    emptylistactors=[]
    for i in item2:
        item=Actor(i+"r")
        emptylistactors.append(item)
        
    arrange_item(emptylistactors)
    animate_items(emptylistactors)
    return emptylistactors
def arrange_item(items_list):
    no_gaps=len(items_list)+1
    gap_size=1000/no_gaps
    for i,item in enumerate(items_list):
        item.x=(i+1)*gap_size
def animate_items(items_list):
    global animation
    for i in items_list:
        time_dur=initial_speed-current_level
        i.anchor=("center", "bottom")
        a=animate(i,duration=time_dur,on_finished=handle_game_over,y=1000)
        animation.append(a)
def handle_game_over():
    global game_over
    game_over=True
def on_mouse_down(pos):
    for i in items_list:
        if i.collidepoint(pos):
            if "green" in i.image:
                handle_game_complete
            else:
                handle_game_over
def handle_game_complete():
    pass
pgzrun.go()