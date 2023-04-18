import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read csv
df = pandas.read_csv("50_states.csv")
state_name = df['state']
state_list = state_name.tolist()


def update_map(x, y, answer_state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(answer_state)


def get_mouse_pos(x, y):
    answer_state = screen.textinput(title="Guess the state", prompt="What is the state name").title()
    if answer_state in state_list:
        data = df[df['state'] == answer_state]
        x_cor, y_cor = int(data.x), int(data.y)
        if abs(x-x_cor) < 200 and abs(y-y_cor)<200:
            update_map(x_cor, x_cor, answer_state)

turtle.onscreenclick(get_mouse_pos)

screen.mainloop()