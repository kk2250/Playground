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
    the entire board on the screen using new_pen.
    It must draw the grid lines as well as
    the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    turtle.resetscreen()
    new_pen = turtle.Turtle()  # creating new pen
    turtle.setworldcoordinates(-50,-50,350,350)
    turtle.bgcolor("black")
    new_pen.color("white")
    new_pen.hideturtle()
    new_pen.left(90) # drawing the board grid
    new_pen.forward(300)
    for i in range(3):
        new_pen.right(90)
        new_pen.forward(300)
    for i in range(100, 301, 200):
        new_pen.right(90)
        new_pen.forward(i)
    for i in range(100, 301, 200):
        new_pen.left(90)
        new_pen.forward(i)
    for i in range(2):
        new_pen.right(90)
        new_pen.forward(100)
    new_pen.right(90)
    new_pen.forward(300)
    for i in range(100, 301, 200):
        new_pen.left(90)
        new_pen.forward(i)
    for i in range(len(the_board)): # drawing the "X" and "O" pieces
        if the_board[i] == "X":
            if i in [0,1,2]: # divide into rows to minimize the code
                new_pen.up()
                new_pen.goto((i*100)+25,225)
                new_pen.setheading(45)
                new_pen.down()
                new_pen.forward(70.71)
                new_pen.up()
                new_pen.goto((i*100)+75,225)
                new_pen.setheading(135)
                new_pen.down()
                new_pen.forward(70.71)
            elif i in [3,4,5]:
                new_pen.up()
                new_pen.goto(((i-3)*100)+25,125)
                new_pen.setheading(45)
                new_pen.down()
                new_pen.forward(70.71)
                new_pen.up()
                new_pen.goto(((i-3)*100)+75,125)
                new_pen.setheading(135)
                new_pen.down()
                new_pen.forward(70.71)
            elif i in [6,7,8]:
                new_pen.up()
                new_pen.goto(((i-6)*100)+25,25)
                new_pen.setheading(45)
                new_pen.down()
                new_pen.forward(70.71)
                new_pen.up()
                new_pen.goto(((i-6)*100)+75,25)
                new_pen.setheading(135)
                new_pen.down()
                new_pen.forward(70.71)
        elif the_board[i] == "O":
            if i in [0,1,2]:  # divide into rows to minimize the code
                new_pen.up()
                new_pen.goto((i*100)+75,250)
                new_pen.setheading(90)
                new_pen.down()
                new_pen.circle(25)
            elif i in [3,4,5]:
                new_pen.up()
                new_pen.goto(((i-3)*100)+75,150)
                new_pen.setheading(90)
                new_pen.down()
                new_pen.circle(25)
            elif i in [6,7,8]:
                new_pen.up()
                new_pen.goto(((i-6)*100)+75,50)
                new_pen.setheading(90)
                new_pen.down()
                new_pen.circle(25)
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
    if 0 < x < 100 and 0 < y < 100 and the_board[6] == "_": # having x and y coordinates to find the right place on board
        the_board[6] = "O"                                  # and the place where player clicks has to be empty space
    elif 0 < x < 100 and 100 < y < 200 and the_board[3] == "_":
        the_board[3] = "O"
    elif 0 < x < 100 and 200 < y < 300 and the_board[0] == "_":
        the_board[0] = "O"
    elif 100 < x < 200 and 0 < y < 100 and the_board[7] == "_":
        the_board[7] = "O"
    elif 100 < x < 200 and 100 < y < 200 and the_board[4] == "_":
        the_board[4] = "O"
    elif 100 < x < 200 and 200 < y < 300 and the_board[1] == "_":
        the_board[1] = "O"
    elif 200 < x < 300 and 0 < y < 100 and the_board[8] == "_":
        the_board[8] = "O"
    elif 200 < x < 300 and 100 < y < 200 and the_board[5] == "_":
        the_board[5] = "O"
    elif 200 < x < 300 and 200 < y < 300 and the_board[2] == "_":
        the_board[2] = "O"
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
    If there is a winner or if there is a stalemate, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    turn = "X"
    for checking in range(2):  # check game over both player and computer with same algorithm
        if checking == 1:
            turn = "O"  # there are only 8 possible patterns to win the game
        if (the_board[0] == turn and the_board[1] == turn and the_board[2] == turn) or \
            (the_board[3] == turn and the_board[4] == turn and the_board[5] == turn) or \
            (the_board[6] == turn and the_board[7] == turn and the_board[8] == turn) or \
            (the_board[0] == turn and the_board[3] == turn and the_board[6] == turn) or \
            (the_board[1] == turn and the_board[4] == turn and the_board[7] == turn) or \
            (the_board[2] == turn and the_board[5] == turn and the_board[8] == turn) or \
            (the_board[0] == turn and the_board[4] == turn and the_board[8] == turn) or \
            (the_board[2] == turn and the_board[4] == turn and the_board[6] == turn):
            if checking == 0: # when 0 the turn is equal to "X" (computer), so game knows that computer is winner
                turtle.goto(150,150)
                turtle.color("red")
                turtle.write("Computer Win!",True,align="center",font=("Arial",30,"bold"))
                for __ in range(len(the_board)): # reset the board
                    the_board[__] = "_"
                time.sleep(2) # hold for 2 seconds, then reset the screen by calling main() function
                main()
                return True
            else:   # when 1 the turn is equal to "O" (player), so game knows that player winner
                turtle.goto(150,150)
                turtle.color("red")
                turtle.write("You Win!",True,align="center",font=("Arial",30,"bold"))
                for __ in range(len(the_board)): # reset the board
                    the_board[__] = "_"
                time.sleep(2)
                main()
                return True
    empty_space = 9
    for X_O in the_board:  # checking the empty spaces
        if X_O == "X" or X_O == "O":
            empty_space -= 1
    if empty_space == 0:  # when the board is full with "X" and "O" and no empty space and no winner, then it's tie
        turtle.goto(150,150)
        turtle.color("red")
        turtle.write("It's a stalemate.",True,align="center",font=("Arial",30,"bold"))
        for _ in range(len(the_board)): # reset the board
            the_board[_] = "_"
        time.sleep(2)
        main()
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
    turn = "X"
    for checking in range(2): # in two iteration, check the winning move first, then the blocking move next using the same algorithm
        if checking == 1:     # total of 24 different ways to check in order to find the right move
            turn = "O"
        if the_board[0] == turn and the_board[1] == turn and the_board[2] == "_":
            the_board[2] = "X"
            return
        elif the_board[0] == turn and the_board[2] == turn and the_board[1] == "_":
            the_board[1] = "X"
            return
        elif the_board[0] == turn and the_board[3] == turn and the_board[6] == "_":
            the_board[6] = "X"
            return
        elif the_board[0] == turn and the_board[4] == turn and the_board[8] == "_":
            the_board[8] = "X"
            return
        elif the_board[0] == turn and the_board[6] == turn and the_board[3] == "_":
            the_board[3] = "X"
            return
        elif the_board[0] == turn and the_board[8] == turn and the_board[4] == "_":
            the_board[4] = "X"
            return
        elif the_board[1] == turn and the_board[2] == turn and the_board[0] == "_":
            the_board[0] = "X"
            return
        elif the_board[1] == turn and the_board[4] == turn and the_board[7] == "_":
            the_board[7] = "X"
            return
        elif the_board[1] == turn and the_board[7] == turn and the_board[4] == "_":
            the_board[4] = "X"
            return
        elif the_board[2] == turn and the_board[4] == turn and the_board[6] == "_":
            the_board[6] = "X"
            return
        elif the_board[2] == turn and the_board[5] == turn and the_board[8] == "_":
            the_board[8] = "X"
            return
        elif the_board[2] == turn and the_board[6] == turn and the_board[4] == "_":
            the_board[4] = "X"
            return
        elif the_board[2] == turn and the_board[8] == turn and the_board[5] == "_":
            the_board[5] = "X"
            return
        elif the_board[3] == turn and the_board[4] == turn and the_board[5] == "_":
            the_board[5] = "X"
            return
        elif the_board[3] == turn and the_board[5] == turn and the_board[4] == "_":
            the_board[4] = "X"
            return
        elif the_board[3] == turn and the_board[6] == turn and the_board[0] == "_":
            the_board[0] = "X"
            return
        elif the_board[4] == turn and the_board[5] == turn and the_board[3] == "_":
            the_board[3] = "X"
            return
        elif the_board[4] == turn and the_board[6] == turn and the_board[2] == "_":
            the_board[2] = "X"
            return
        elif the_board[4] == turn and the_board[7] == turn and the_board[1] == "_":
            the_board[1] = "X"
            return
        elif the_board[4] == turn and the_board[8] == turn and the_board[0] == "_":
            the_board[0] = "X"
            return
        elif the_board[5] == turn and the_board[8] == turn and the_board[2] == "_":
            the_board[2] = "X"
            return
        elif the_board[6] == turn and the_board[7] == turn and the_board[8] == "_":
            the_board[8] = "X"
            return
        elif the_board[6] == turn and the_board[8] == turn and the_board[7] == "_":
            the_board[7] = "X"
            return
        elif the_board[7] == turn and the_board[8] == turn and the_board[6] == "_":
            the_board[6] = "X"
            return
    empty_space = 9
    while empty_space > 0:  # except the must-do move, next computer move will be randomly selected
        empty_space = 9
        for X_O in the_board: #checking the empty spaces
            if X_O == "X" or X_O == "O":
                empty_space -= 1
        com_m = random.randint(0,8)
        if the_board[com_m] == "_": # additionaly, check if that random place is empty
            the_board[com_m] = "X"
            break

def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by new_pen in response
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
    turtle.mainloop()

main()