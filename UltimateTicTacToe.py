board = [[''] * 3 for _ in range(3)]
isX = True

def printBoard():
    for i, row in enumerate(board):
        cells = [cell if cell != '' else ' ' for cell in row]
        print(' ' + ' | '.join(cells) + ' ')
        if i < 2:
            print('---+---+---')
    print()

def checkWin(sign):
    goal = sign * 3
    for row in board:
        if row == goal:
            return True
    curr = ''
    rcurr = ''
    for c in range(3):
        for r in range(3):
            curr+= board[r][c]
        if curr == goal:
            return True
        
        curr = ''
    
    curr = ''
    rcurr = ''
    
    for r in range(3):
        curr+= board[r][r]
        rcurr+= board[r][3-r-1]
    
    if curr == goal or rcurr == goal:
        return True
    
    return False
    

def isValid(r,c, sign):
    if board[r][c] == '':
        board[r][c] = sign
        printBoard()
        return True
    
    else:
        print('!!!Enter valid move!!!\n')
        printBoard()
        return False


def play():
    global isX

    while isX:
        tot = input('X to play  :  ')
        r,c = tot.split(',')
        r,c = int(r), int(c)
        if isValid(r,c, 'X'):
            isX = False
        
        if checkWin('X'):
            print('X is the winner')
            return 
        
        full = True
        for r in board:
            if '' in r:
                full = False
        
        if full:
            print('Draw')
            return 
    
    # printBoard()

        
        
    while not isX:
        tot = input('O to play  :  ')
        r,c = tot.split(',')
        r,c = int(r), int(c)
        if isValid(r,c,'O'):
            isX = True
        
        if  checkWin('O'):
            print('O is the winner')
            return 
        
        full = True
        for r in board:
            if '' in r:
                full = False
        
        if full:
            print('Draw')
            return 
        
        
    printBoard()

    play()
        
play()
    



