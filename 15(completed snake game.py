import pygame as pg 
import random
pg.init()
screen_width=1200
screen_height=600
gamewindow=pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("snake game")






clock=pg.time.Clock()

print(clock)
#color defining
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
font=pg.font.SysFont(None,30)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
            pg.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])




def gameloop():
    with open("highscore.txt",'r') as f:     
     hscore=f.read()
    
    score=0
    food_size=20
    fps=60
    velocity_x=0
    velocity_y=0
    food_x=random.randint(50,screen_width-100)
    food_y=random.randint(50,screen_height-200)
    snake_x=45
    snake_y=55
    snake_size=20
    velocity=5
    a=velocity
    snk_list=[]
    snk_length=1
    #giving contron directive velocity to snake
    exit_game=False
    game_over=False
    while not exit_game :
        if game_over:        
                gamewindow.fill(white)
                text_screen("Game over press enter to play again",red,300,200)
                text_screen("Current score:"+str(score),red,400,250)
                text_screen(f"highest score: {hscore}",red,400,300)
                for event in pg.event.get():
                    if event.type==pg.QUIT:
                        exit_game=True
                    elif event.type==pg.KEYDOWN:
                        if event.key==pg.K_RETURN:
                            gameloop() 
                      
        else:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    exit_game=True
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RIGHT:
                        velocity_x=a
                        velocity_y=0
                    elif event.key==pg.K_DOWN:
                        velocity_y=a
                        velocity_x=0
                    elif event.key==pg.K_LEFT:
                        velocity_x=-a
                        velocity_y=0
                    elif event.key==pg.K_UP:
                        velocity_y=-a
                        velocity_x=0
            #giving velocity to snake
            snake_x=snake_x +velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score+=10
                snk_length+=5
                food_x=random.randint(20,screen_width)
                food_y=random.randint(20,screen_height)
                if score>int(hscore):
                     with open("highscore.txt","w") as f:
                          f.write(str(score))
                          
                with open("highscore.txt",'r') as f:     
                   hscore=f.read()
                
               
                

            gamewindow.fill(white)
            text_screen("score: "+str(score),green,5,5)
            text_screen("highest: "+hscore,green,5,25)
            
            # making snake food
            pg.draw.rect(gamewindow,green,[food_x,food_y,food_size,food_size]) 
            
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                        game_over=True 
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                

            #pg.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gamewindow,black,snk_list,snake_size)
        pg.display.update() 
        clock.tick(fps)
        
        
        
    pg.quit()
    quit()


gameloop()