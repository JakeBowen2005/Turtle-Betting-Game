import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=275)
        self.write(arg=f"Score:  {self.score}", move=False, font=("Arial", 24, "normal"), align="Center")

    def changeScore(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:  {self.score}", move=False, font=("Arial", 20, "normal"), align="Center")

    def GameOver(self):
        game_over = t.Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color("Green")
        game_over.write("Game Over", align="center", font=("Arial", 30, "normal"))