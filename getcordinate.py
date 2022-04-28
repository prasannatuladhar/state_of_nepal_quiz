import turtle
screen = turtle.Screen()
def get_mouse_click_coor(x, y):
    print(x, y)


image = "C://Users/User/Desktop/book/state_of_nepal_quiz/state_of_nepal_quiz/map_of_nepal_1.gif"
screen.addshape(image)
turtle.shape(image)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()