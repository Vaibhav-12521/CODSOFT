import tkinter as tk
import tkinter.messagebox as msg
import random
import math

MAN = '⭕' 
AI = '❌'
EMPTY = ''

board = [
  [EMPTY, EMPTY, EMPTY],
  [EMPTY, EMPTY, EMPTY],
  [EMPTY, EMPTY, EMPTY]
]

buttons  = [
  [EMPTY, EMPTY, EMPTY],
  [EMPTY, EMPTY, EMPTY],
  [EMPTY, EMPTY, EMPTY]
]


score = {"Player": 0, "AI": 0, "Draw": 0}
difficulty = "Hard" 

def level():
    global difficulty
    if difficulty == "Hard":
        difficulty = "Easy"
    else:
        difficulty = "Hard"
    difficulty_btn.config(text=f"Mode: {difficulty}")


def chk_win(b):
    lines = [
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[2][0], b[1][1], b[0][2]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] != EMPTY:
            return line[0]
    if all(cell != EMPTY for row in b for cell in row):
        return "Draw"
    return None

def AI_MOVE():
    
    if difficulty == "Easy":
        choices = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    choices.append((i, j))
        if choices:
            return random.choice(choices)
        else:
            return None

    else:
        best_val = -math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    val = mini(board, -math.inf, math.inf, False)
                    board[i][j] = EMPTY
                    if val > best_val:
                        best_val = val
                        move = (i, j)
        return move


def mini(b, apl, bta, is_max):
    winner = chk_win(b)
    if winner == AI: 
        return 1
    if winner == MAN: 
        return -1
    if winner == "Draw": 
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    val = mini(b, apl, bta, False)
                    b[i][j] = EMPTY
                    best = max(best, val)
                    apl = max(apl, val)
                    if bta <= apl:
                        break
        return best
    else:
        worst = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = MAN
                    val = mini(b, apl, bta, True)
                    b[i][j] = EMPTY
                    worst = min(worst, val)
                    bta = min(bta, val)
                    if bta <= apl:
                        break
        return worst

def last(result):
    if result == "Draw":
        score["Draw"] += 1
        msg.showinfo("Result", "It's a Draw!")
    elif result == MAN:
        score["Player"] += 1
        msg.showinfo("Result", "You Win!")
    else:
        score["AI"] += 1
        msg.showinfo("Result", "AI Wins!")
    updt_scr()
    RESTART()

def on_click(i, j):
    if board[i][j] == EMPTY and chk_win(board) is None:
        board[i][j] = MAN
        buttons[i][j].config(text=MAN, fg='blue')
        result = chk_win(board)
        if result:
            last(result)
            return
        ai_move = AI_MOVE()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = AI
            buttons[ai_move[0]][ai_move[1]].config(text=AI, fg='red')
        result = chk_win(board)
        if result:
            last(result)


def RESTART():
    for i in range(3):
        for j in range(3):
            board[i][j] = EMPTY
            buttons[i][j].config(text=EMPTY)

def updt_scr():
    score_label.config(text=f"Player: {score['Player']} | AI: {score['AI']} | Draw: {score['Draw']}")


root = tk.Tk()
root.title("Tic-Tac-Toe Game")
icon = tk.PhotoImage(file='game.png')
root.iconphoto(True, icon)


for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text=EMPTY, font=('Arial', 40), width=3, height=1,
                        command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

score_label = tk.Label(root, text="", font=('Arial', 14))
score_label.grid(row=3, column=0, columnspan=3)
updt_scr()

reset_btn = tk.Button(root, text="Reset", command=RESTART, bg='lightgray')
reset_btn.grid(row=4, column=0, columnspan=1, sticky='nsew')

difficulty_btn = tk.Button(root, text=f"Mode: {difficulty}", command=level, bg='lightblue')
difficulty_btn.grid(row=4, column=1, columnspan=2, sticky='nsew')

root.mainloop()
