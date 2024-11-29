from os import write
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(y=270, x=0)
        self.write(f"Score: {self.score}",align="center",font=("Arial",18,"normal"))
        self.hideturtle()
        with open("data.txt") as data:
            self.highscore =int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.highscore}", align="center", font=("Arial", 18, "normal"))



    def reset(self):
        self.clear()
        if self.score> self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="Game over",align="center",font=("Arial", 30, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High score {self.highscore}", align="center", font=("Arial", 18, "normal"))
