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
    pass # your code here
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
    pass # your code here

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
    pass # your code here

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
    pass # your code here

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
    turtle.mainloop()

main()
