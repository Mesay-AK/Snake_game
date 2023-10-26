from turtle import Screen
from Snake import Snake
import time
from food import food
from scoreboard import scoreboard

Screen=Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor('black')
Screen.title("Snake Game")

Screen.tracer(0)

snake = Snake()
food=food()
scoreboard=scoreboard()

Screen.listen()
Screen.onkey(snake.up,'Up')
Screen.onkey(snake.down,'Down')
Screen.onkey(snake.left,'Left')
Screen.onkey(snake.right,'Right')



game_is_on = True
while game_is_on:
    Screen.update()
    time.sleep(0.1)
    snake.move()

# Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detect Collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False 
        scoreboard.game_over()

# Detect Collision with tail: if head collies with any segment in the tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()





Screen.exitonclick()


