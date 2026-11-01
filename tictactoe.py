import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

currentPlayer = "X"
board = ["-"] * 9
buttons = []
winner = None

def check_winner():
    global winner
    wins = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diags
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != "-":
            winner = board[a]
            return True
    return False

def check_tie():
    return "-" not in board and winner is None

def computer_move():
    empty = [i for i, v in enumerate(board) if v == "-"]
    if empty:
        pos = random.choice(empty)
        board[pos] = "O"
        buttons[pos].config(text="O", state="disabled")
        if check_winner():
            status.config(text="O wins!")
            disable_all()
        elif check_tie():
            status.config(text="It's a tie!")

def on_click(i):
    global currentPlayer
    if board[i] == "-" and winner is None:
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        if check_winner():
            status.config(text="X wins!")
            disable_all()  
        elif check_tie():
            status.config(text="It's a tie!")
        else:
            root.after(500, computer_move)

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

# Create buttons
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 32), width=3, height=1,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status = tk.Label(root, text="Your turn (X)", font=("Arial", 16))
status.grid(row=3, column=0, columnspan=3)

root.mainloop()