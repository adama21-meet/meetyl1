import turtle
import random

turtle.tracer(1,0)

#turtle placement
size_x=800
size_y=500
turtle.setup(size_x,size_y)

turtle.penup()

#turtle design
square_size=20
start_legnth=6
time_step=100

#lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

#set up positions
snake=turtle.clone()
snake.shape('square')
turtle.hideturtle()

#Function to draw a part of the snake on the screen
def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos) 
    my_stamp= snake.stamp()
    stamp_list.append(my_stamp)


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(start_legnth) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=square_size

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp


turtle.mainloop()
