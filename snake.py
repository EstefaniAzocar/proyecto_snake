from turtle import Turtle

#Construir cuerpo serpiente
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    #Constructor
    def __init__(self):
        #Almaceno los segementos de la serpiente
        self.segments = []
        #Metodo que crea la serpiente
        self.create_snake()
        #Atributo cabeza
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0, -1):

            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
   