def display_board(board):
    print("The board now: \n")
    k = 0
    while k<9:
        print(board[k],end = "")
        k+=1
        if (k%3 != 0):
            print(" | ",end = "")
        else:
            print("\n")
    
    pass

def player_input():
    k = 1
    while k==1:
        p = int(input('Please enter a number: '))
        if p in range(1,9):
            k+=1
    return p

def place_marker(board, marker, position):
    board[position-1] = marker
    pass

def win_check(b, m):
    l = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,1,8],[2,4,6]]
    k = 0
    for i in l:
        p = 0
        for j in i:
            if b[j] == m:
                p+=1
        if p==3:
            k+=1
    if k>0:
        return True
    else:
        return False
    
    pass

import random

def choose_first():
    p = random.randint(1,2)
    print("Player {} goes first".format(p))
    pass

def space_check(board, position):
    if board[position-1] == '#':
        return True
    else:
        return False
    
    pass

def full_board_check(board):
    k = 0
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    
    pass

def player_choice(board):

    k = 0
    while k == 0:
        p = int(input("Choose your position: "))
        if p not in range(1,10):
            continue
        if p == 0:
           display_board(board)
           continue 
        if space_check(board,p):
            k+=1
            return p
            pass
        else:
            print("That's already taken. ")
     
    pass

def replay():
    p = input("You wanna play again? ;) (y,n) ")
    if p == 'y' or p == 'Y':
        return True
    else:
        return False
    
    pass


print('Welcome to Tic Tac Toe! \n')

while True:
    
    board = ['#','#','#','#','#','#','#','#','#']
    display_board(board)
    print("\n"*2)
    choose_first()
    pl = 1
    won = 0
    while full_board_check != 1:
        
        p = player_choice(board)
        if pl%2 != 0:
            place_marker(board, 'X', p)
        else:
            place_marker(board, 'O', p)
        
        pl+=1
        print("\n"*2)
        display_board(board)
        win1 = win_check(board, 'X')
        win2 = win_check(board, 'O')
        

        if win1:
            print("{} has won".format('X'))
            won+=1
            break
        elif win2:
            print("{} has won".format('O'))
            won+=1
            break
        else:
            won = 0
            print("Continue.")

        if pl == 10 or full_board_check == 1:
            print("That's a draw.")
            break

          
    r = replay()
    if r == 1:
        print("That's great. ")
    else:
        print("Come back soon.")
        break







    



    
    
