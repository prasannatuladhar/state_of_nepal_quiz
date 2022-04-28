import turtle
import pandas

screen = turtle.Screen()

image = "C://Users/User/Desktop/book/state_of_nepal_quiz/state_of_nepal_quiz/map_of_nepal_1.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("All The States of Nepal")


us_state= pandas.read_csv("C://Users/User/Desktop/book/state_of_nepal_quiz/state_of_nepal_quiz/state_info.csv")
state_list=us_state.state.to_list()

is_quiz_over = False
user_guess_list=[]

while not is_quiz_over:
    
    user_answer_statename = turtle.textinput(f"{len(user_guess_list)}/{len(state_list)} Correctly Guessed","write the name of every state").title()

    if user_answer_statename in state_list:
        
        t_writer = turtle.Turtle()
        data = us_state[us_state.state==user_answer_statename]
        x=int(data.x)
        y=int(data.y)
        t_writer.hideturtle()

        t_writer.penup()
        t_writer.goto(x,y)
        t_writer.write(user_answer_statename)
        
        
        if user_answer_statename not in user_guess_list:
            user_guess_list.append(user_answer_statename)
    
    if len(user_guess_list)==len(state_list):
        t_writer.goto(-136.0 ,-182.0)
        t_writer.write("Well Done! You have guessed all the name of state correctly")
        is_quiz_over=True
       

    if user_guess_list == "Exit":
        break



turtle.mainloop()