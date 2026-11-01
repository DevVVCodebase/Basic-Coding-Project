from tkinter import *
import random

GAMEWIDTH = 600
GAMEHEIGHT = 400
SPEED = 100
SNAKE_SIZE = 20
BODYPART = 3
SNAKE_COLOR = "green"
FOODCOLOR = "red"
BACKGROUND_COLOR = "black"

def change_direction(new_direction):
    opposites = {"up":"down", "down":"up", "left":"right", "right":"left"}
    if opposites.get(new_direction) != snake.direction:
        snake.direction = new_direction

class SnakeGame:
    def __init__(self):
        self.bodysize = BODYPART
        self.coordinates = []
        self.square = []
        self.direction = "down"
        for i in range(self.bodysize):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_COLOR)
            self.square.append(square)

class Food:
    def __init__(self):
        self.x = random.randint(0, (GAMEWIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.y = random.randint(0, (GAMEHEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.color = FOODCOLOR
        self.size = SNAKE_SIZE
        self.coordinates = [self.x, self.y]
        self.food = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color, outline=self.color)

def next_turn(snake, food):
    global score

    x, y = snake.coordinates[0]
    if snake.direction == "up":
        y -= SNAKE_SIZE
    elif snake.direction == "down":
        y += SNAKE_SIZE
    elif snake.direction == "left":
        x -= SNAKE_SIZE
    elif snake.direction == "right":
        x += SNAKE_SIZE

    new_head = [x, y]

    # Check for collisions
    if (
        x < 0 or x >= GAMEWIDTH or
        y < 0 or y >= GAMEHEIGHT or
        new_head in snake.coordinates
    ):
        game_over()
        return

    snake.coordinates.insert(0, new_head)
    square = canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR, outline=SNAKE_COLOR)
    snake.square.insert(0, square)

    # Check if food is eaten
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete(food.food)
        food.__init__()  # Create new food
    else:
        # Remove tail
        del snake.coordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]

    window.after(SPEED, next_turn, snake, food)

def restart_game():
    global snake, food, score
    for square in snake.square:
        canvas.delete(square)
    canvas.delete(food.food)
    canvas.delete("gameover")
    score = 0
    label.config(text=f"Score: {score}")
    snake = SnakeGame()
    food = Food()
    next_turn(snake, food)

def game_over():
    canvas.create_text(
        GAMEWIDTH // 2,
        GAMEHEIGHT // 2,
        font=("consolas", 40),
        text="GAME OVER",
        fill="red",
        tags="gameover"
    )

window = Tk()
window.title("Snake Game")
window.resizable(False, False)
score = 0

# Use a frame to stack widgets vertically
main_frame = Frame(window)
main_frame.pack()

# Horizontal frame for score and restart button
top_frame = Frame(main_frame)
top_frame.pack()

label = Label(top_frame, text=f"Score: {score}", font=("consolas", 40))
label.pack(side=LEFT, padx=10)

restart_btn = Button(top_frame, text="Restart", font=("consolas", 20), command=restart_game)
restart_btn.pack(side=LEFT, padx=10)

canvas = Canvas(main_frame, background=BACKGROUND_COLOR, width=GAMEWIDTH, height=GAMEHEIGHT)
canvas.pack()

# Set window size to fit all widgets
total_height = 40 + GAMEHEIGHT + 60  # label + canvas + button + padding
window.geometry(f"{GAMEWIDTH}x{total_height}")

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{GAMEWIDTH}x{total_height}+{x}+{y}")

snake = SnakeGame()
food = Food()

window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

next_turn(snake, food)
window.mainloop()