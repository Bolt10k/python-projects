import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIAN STATE GAME")
image ="india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
guessed_state = []
all_state = [state.title() for state in data.state.to_list()]

while len(guessed_state) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28 states correct", prompt="Enter state name")
    if  answer_state=="exit":
        missing_states = []
        for state in  all_state:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    answer_state = answer_state.title()
    if answer_state in all_state and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center",font=("Arial",12,"bold"))

screen.exitonclick()

