from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
SFILE = 'D:\Zohaib Tahir\PyCharm Project\Snake game\high_score.txt'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(SFILE, mode='a+') as file:
            try: 
                self.high_score = int(file.read())
            except:
                self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score} ', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SFILE, mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
            self.score += 1
            self.update_scoreboard()
