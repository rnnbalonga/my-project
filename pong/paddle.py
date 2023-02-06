from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.color("black")
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        This function will make the paddle go up.
        """
        new_y = self.ycor() + 20
        #After testing 260 is the limit before the paddle moves offscreen.
        if new_y <= 260:
            self.goto(self.xcor(),new_y)
        else:
            pass
    
    def go_down(self):
        """
        This function will make the paddle go down.
        """
        new_y = self.ycor() - 20
        #After testing -240 is the limit before the paddle moves offscreen.
        if new_y >= -240:
            self.goto(self.xcor(),new_y)
        else:
            pass