import turtle
import pandas

#setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#panda usage
data = pandas.read_csv("50_states.csv")
guessed_state = []
all_state = [state.title() for state in data.state.to_list()]

#loop
while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 States Correct", "Enter a state name:")
    if  answer_state=="exit":
        missing_states = []
        for state in  all_state:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")# to make file of states that are not guessed
        break
    #main
    answer_state = answer_state.title()
    if answer_state in all_state and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center")

screen.exitonclick()

