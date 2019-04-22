# CS-UY 1114
# Final project

import turtle
import time
import random

# This list represents the state of the
# board. It's a list of nine strings,
# each of which is either "X", "O", "_",
# representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def draw_board(board):
    """
    signature: list(str) -> NoneType
    The current state of the board, indicating
    the position of all pieces, is given
    as a parameter. This function should draw
    the entire board on the screen using turtle.
    It must draw the grid lines as well as
    the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    qwert = turtle.Turtle()
    turtle.setworldcoordinates(-50,-50,350,350)
    turtle.bgcolor("black")
    qwert.color("white")
    qwert.hideturtle()
    # qwert.speed()
    qwert.left(90)
    qwert.forward(300)
    for i in range(3):
        qwert.right(90)
        qwert.forward(300)
    for i in range(100, 301, 200):
        qwert.right(90)
        qwert.forward(i)
    for i in range(100, 301, 200):
        qwert.left(90)
        qwert.forward(i)
    for i in range(2):
        qwert.right(90)
        qwert.forward(100)
    qwert.right(90)
    qwert.forward(300)
    for i in range(100, 301, 200):
        qwert.left(90)
        qwert.forward(i)
    for i in range(len(the_board)):
        if the_board[i] == "X":
            if i in [0,1,2]:
                qwert.penup()
                qwert.setposition((i*100)+25,225)
                qwert.setheading(45)
                qwert.pendown()
                qwert.forward(70.71)
                qwert.penup()
                qwert.setposition((i*100)+75,225)
                qwert.setheading(135)
                qwert.pendown()
                qwert.forward(70.71)
            elif i in [3,4,5]:
                qwert.penup()
                qwert.setposition(((i-3)*100)+25,125)
                qwert.setheading(45)
                qwert.pendown()
                qwert.forward(70.71)
                qwert.penup()
                qwert.setposition(((i-3)*100)+75,125)
                qwert.setheading(135)
                qwert.pendown()
                qwert.forward(70.71)
            elif i in [6,7,8]:
                qwert.penup()
                qwert.setposition(((i-6)*100)+25,25)
                qwert.setheading(45)
                qwert.pendown()
                qwert.forward(70.71)
                qwert.penup()
                qwert.setposition(((i-6)*100)+75,25)
                qwert.setheading(135)
                qwert.pendown()
                qwert.forward(70.71)
        elif the_board[i] == "O":
            if i in [0,1,2]:
                qwert.penup()
                qwert.setposition((i*100)+75,250)
                qwert.setheading(90)
                qwert.pendown()
                qwert.circle(25)
            elif i in [3,4,5]:
                qwert.penup()
                qwert.setposition(((i-3)*100)+75,150)
                qwert.setheading(90)
                qwert.pendown()
                qwert.circle(25)
            elif i in [6,7,8]:
                qwert.penup()
                qwert.setposition(((i-6)*100)+75,50)
                qwert.setheading(90)
                qwert.pendown()
                qwert.circle(25)
    turtle.update()

def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    The current state of the board is given as
    a parameter, as well as the x,y screen coordinate
    indicating where the user clicked. This function
    should update the board state variable
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool, indicating if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """
    print("user clicked at "+str(x)+","+str(y))
    if 0 < x < 100:
        if 0 < y < 100:
            if the_board[6] == "_":
                the_board[6] = "O"
            else:
                return False
        elif 100 < y < 200:
            if the_board[3] == "_":
                the_board[3] = "O"
            else:
                return False
        elif 200 < y < 300:
            if the_board[0] == "_":
                the_board[0] = "O"
            else:
                return False
        else:
            return False
    elif 100 < x < 200:
        if 0 < y < 100:
            if the_board[7] == "_":
                the_board[7] = "O"
            else:
                return False
        elif 100 < y < 200:
            if the_board[4] == "_":
                the_board[4] = "O"
            else:
                return False
        elif 200 < y < 300:
            if the_board[1] == "_":
                the_board[1] = "O"
            else:
                return False
        else:
            return False
    elif 200 < x < 300:
        if 0 < y < 100:
            if the_board[8] == "_":
                the_board[8] = "O"
            else:
                return False
        elif 100 < y < 200:
            if the_board[5] == "_":
                the_board[5] = "O"
            else:
                return False
        elif 200 < y < 300:
            if the_board[2] == "_":
                the_board[2] = "O"
            else:
                return False
        else:
            return False
    else:
        return False
    return True

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    ii = "X"
    if the_board[0] == ii:
        if the_board[1] == ii:
            if the_board[2] == ii:
                print("Computer WIN!!")
                return True
        if the_board[3] == ii:
            if the_board[6] == ii:
                print("Computer WIN!!")
                return True
        if the_board[4] == ii:
            if the_board[8] == ii:
                print("Computer WIN!!")
                return True
    if the_board[1] == ii:
        if the_board[4] == ii:
            if the_board[7] == ii:
                print("Computer WIN!!")
                return True
    if the_board[2] == ii:
        if the_board[5] == ii:
            if the_board[8] == ii:
                print("Computer WIN!!")
                return True
        if the_board[4] == ii:
            if the_board[6] == ii:
                print("Computer WIN!!")
                return True
    if the_board[3] == ii:
        if the_board[4] == ii:
            if the_board[5] == ii:
                print("Computer WIN!!")
                return True
    if the_board[6] == ii:
        if the_board[7] == ii:
            if the_board[8] == ii:
                print("Computer WIN!!")
                return True
    ii = "O"
    if the_board[0] == ii:
        if the_board[1] == ii:
            if the_board[2] == ii:
                print("You WIN!!")
                return True
        if the_board[3] == ii:
            if the_board[6] == ii:
                print("You WIN!!")
                return True
        if the_board[4] == ii:
            if the_board[8] == ii:
                print("You WIN!!")
                return True
    if the_board[1] == ii:
        if the_board[4] == ii:
            if the_board[7] == ii:
                print("You WIN!!")
                return True
    if the_board[2] == ii:
        if the_board[5] == ii:
            if the_board[8] == ii:
                print("You WIN!!")
                return True
        if the_board[4] == ii:
            if the_board[6] == ii:
                print("You WIN!!")
                return True
    if the_board[3] == ii:
        if the_board[4] == ii:
            if the_board[5] == ii:
                print("You WIN!!")
                return True
    if the_board[6] == ii:
        if the_board[7] == ii:
            if the_board[8] == ii:
                print("You WIN!!")
                return True
    x = 0
    for _ in the_board:
        if _ == "X" or _ == "O":
            x += 1
    if x == 9:
        print("It's a stalemate.")
        return True

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    ii = "x"
    for i in range(2):
        if i == 1:
            ii = "O"
        if the_board[0] == ii:
            if the_board[1] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
            if the_board[2] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
            if the_board[3] == ii:
                if the_board[6] == "_":
                    the_board[6] = "X"
                    return
            if the_board[4] == ii:
                if the_board[8] == "_":
                    the_board[8] = "X"
                    return
            if the_board[6] == ii:
                if the_board[3] == "_":
                    the_board[3] = "X"
                    return
            if the_board[8] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
        if the_board[1] == ii:
            if the_board[0] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
            if the_board[2] == ii:
                if the_board[0] == "_":
                    the_board[0] = "X"
                    return
            if the_board[4] == ii:
                if the_board[7] == "_":
                    the_board[7] = "X"
                    return
            if the_board[7] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
        if the_board[2] == ii:
            if the_board[0] == ii:
                if the_board[1] == "_":
                    the_board[1] = "X"
                    return
            if the_board[1] == ii:
                if the_board[0] == "_":
                    the_board[0] = "X"
                    return
            if the_board[4] == ii:
                if the_board[6] == "_":
                    the_board[6] = "X"
                    return
            if the_board[5] == ii:
                if the_board[8] == "_":
                    the_board[8] = "X"
                    return
            if the_board[6] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
            if the_board[8] == ii:
                if the_board[5] == "_":
                    the_board[5] = "X"
                    return
        if the_board[3] == ii:
            if the_board[0] == ii:
                if the_board[6] == "_":
                    the_board[6] = "X"
                    return
            if the_board[4] == ii:
                if the_board[5] == "_":
                    the_board[5] = "X"
                    return
            if the_board[5] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
            if the_board[6] == ii:
                if the_board[0] == "_":
                    the_board[0] = "X"
                    return
        if the_board[4] == ii:
            if the_board[0] == ii:
                if the_board[8] == "_":
                    the_board[8] = "X"
                    return
            if the_board[1] == ii:
                if the_board[7] == "_":
                    the_board[7] = "X"
                    return
            if the_board[2] == ii:
                if the_board[6] == "_":
                    the_board[6] = "X"
                    return
            if the_board[3] == ii:
                if the_board[5] == "_":
                    the_board[5] = "X"
                    return
            if the_board[5] == ii:
                if the_board[3] == "_":
                    the_board[3] = "X"
                    return
            if the_board[6] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
            if the_board[7] == ii:
                if the_board[1] == "_":
                    the_board[1] = "X"
                    return
            if the_board[8] == ii:
                if the_board[0] == "_":
                    the_board[0] = "X"
                    return
        if the_board[5] == ii:
            if the_board[2] == ii:
                if the_board[8] == "_":
                    the_board[8] = "X"
                    return
            if the_board[3] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
            if the_board[4] == ii:
                if the_board[3] == "_":
                    the_board[3] = "X"
                    return
            if the_board[8] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
        if the_board[6] == ii:
            if the_board[0] == ii:
                if the_board[3] == "_":
                    the_board[3] = "X"
                    return
            if the_board[2] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
            if the_board[3] == ii:
                if the_board[0] == "_":
                    the_board[0] = "X"
                    return
            if the_board[4] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
            if the_board[7] == ii:
                if the_board[8] == "_":
                    the_board[8] = "X"
                    return
            if the_board[8] == ii:
                if the_board[7] == "_":
                    the_board[7] = "X"
                    return
        if the_board[7] == ii:
            if the_board[1] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
            if the_board[4] == ii:
                if the_board[1] == "_":
                    the_board[1] = "X"
                    return
            if the_board[6] == ii:
                if the_board[8] == "_":
                    the_board[8] = "X"
                    return
            if the_board[8] == ii:
                if the_board[6] == "_":
                    the_board[6] = "X"
                    return
        if the_board[8] == ii:
            if the_board[0] == ii:
                if the_board[4] == "_":
                    the_board[4] = "X"
                    return
            if the_board[2] == ii:
                if the_board[5] == "_":
                    the_board[5] = "X"
                    return
            if the_board[4] == ii:
                if the_board[0] == "_":
                    the_board[0] = "X"
                    return
            if the_board[5] == ii:
                if the_board[2] == "_":
                    the_board[2] = "X"
                    return
            if the_board[6] == ii:
                if the_board[7] == "_":
                    the_board[7] = "X"
                    return
            if the_board[7] == ii:
                if the_board[6] == "_":
                    the_board[6] = "X"
                    return
    # ii = "O"
    # if the_board[0] == ii:
    #     if the_board[1] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    #     if the_board[2] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    #     if the_board[3] == ii:
    #         if the_board[6] == "_":
    #             the_board[6] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[8] == "_":
    #             the_board[8] = "X"
    #             return
    #     if the_board[6] == ii:
    #         if the_board[3] == "_":
    #             the_board[3] = "X"
    #             return
    #     if the_board[8] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    # if the_board[1] == ii:
    #     if the_board[0] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    #     if the_board[2] == ii:
    #         if the_board[0] == "_":
    #             the_board[0] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[7] == "_":
    #             the_board[7] = "X"
    #             return
    #     if the_board[7] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    # if the_board[2] == ii:
    #     if the_board[0] == ii:
    #         if the_board[1] == "_":
    #             the_board[1] = "X"
    #             return
    #     if the_board[1] == ii:
    #         if the_board[0] == "_":
    #             the_board[0] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[6] == "_":
    #             the_board[6] = "X"
    #             return
    #     if the_board[5] == ii:
    #         if the_board[8] == "_":
    #             the_board[8] = "X"
    #             return
    #     if the_board[6] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    #     if the_board[8] == ii:
    #         if the_board[5] == "_":
    #             the_board[5] = "X"
    #             return
    # if the_board[3] == ii:
    #     if the_board[0] == ii:
    #         if the_board[6] == "_":
    #             the_board[6] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[5] == "_":
    #             the_board[5] = "X"
    #             return
    #     if the_board[5] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    #     if the_board[6] == ii:
    #         if the_board[0] == "_":
    #             the_board[0] = "X"
    #             return
    # if the_board[4] == ii:
    #     if the_board[0] == ii:
    #         if the_board[8] == "_":
    #             the_board[8] = "X"
    #             return
    #     if the_board[1] == ii:
    #         if the_board[7] == "_":
    #             the_board[7] = "X"
    #             return
    #     if the_board[2] == ii:
    #         if the_board[6] == "_":
    #             the_board[6] = "X"
    #             return
    #     if the_board[3] == ii:
    #         if the_board[5] == "_":
    #             the_board[5] = "X"
    #             return
    #     if the_board[5] == ii:
    #         if the_board[3] == "_":
    #             the_board[3] = "X"
    #             return
    #     if the_board[6] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    #     if the_board[7] == ii:
    #         if the_board[1] == "_":
    #             the_board[1] = "X"
    #             return
    #     if the_board[8] == ii:
    #         if the_board[0] == "_":
    #             the_board[0] = "X"
    #             return
    # if the_board[5] == ii:
    #     if the_board[2] == ii:
    #         if the_board[8] == "_":
    #             the_board[8] = "X"
    #             return
    #     if the_board[3] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[3] == "_":
    #             the_board[3] = "X"
    #             return
    #     if the_board[8] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    # if the_board[6] == ii:
    #     if the_board[0] == ii:
    #         if the_board[3] == "_":
    #             the_board[3] = "X"
    #             return
    #     if the_board[2] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    #     if the_board[3] == ii:
    #         if the_board[0] == "_":
    #             the_board[0] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    #     if the_board[7] == ii:
    #         if the_board[8] == "_":
    #             the_board[8] = "X"
    #             return
    #     if the_board[8] == ii:
    #         if the_board[7] == "_":
    #             the_board[7] = "X"
    #             return
    # if the_board[7] == ii:
    #     if the_board[1] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[1] == "_":
    #             the_board[1] = "X"
    #             return
    #     if the_board[6] == ii:
    #         if the_board[8] == "_":
    #             the_board[8] = "X"
    #             return
    #     if the_board[8] == ii:
    #         if the_board[6] == "_":
    #             the_board[6] = "X"
    #             return
    # if the_board[8] == ii:
    #     if the_board[0] == ii:
    #         if the_board[4] == "_":
    #             the_board[4] = "X"
    #             return
    #     if the_board[2] == ii:
    #         if the_board[5] == "_":
    #             the_board[5] = "X"
    #             return
    #     if the_board[4] == ii:
    #         if the_board[0] == "_":
    #             the_board[0] = "X"
    #             return
    #     if the_board[5] == ii:
    #         if the_board[2] == "_":
    #             the_board[2] = "X"
    #             return
    #     if the_board[6] == ii:
    #         if the_board[7] == "_":
    #             the_board[7] = "X"
    #             return
    #     if the_board[7] == ii:
    #         if the_board[6] == "_":
    #             the_board[6] = "X"
    #             return
    x = 0
    while x < 9:
        x = 0
        for _ in the_board:
            if _ == "X" or _ == "O":
                x += 1
        com_m = random.randint(0,8)
        if the_board[com_m] == "_":
            the_board[com_m] = "X"
            break
    return

def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    print(1)
    turtle.mainloop()
    print(2)

main()