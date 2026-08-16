
def checkWin(sign, board):
    goal = sign * 3
    for row in board: 
        if row == [sign, sign, sign]:
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

def isValidPlay(r,c, sign, board):
    if board[r][c] == '':
        board[r][c] = sign
        printBoard()
        return True
    
    else:
        print('!!!Enter valid move!!!\n')
        printBoard()
        return False
    
def isValidGrid(grid_row, grid_col):
    if meta_board[grid_row][grid_col] == '':
        return True
    print('Invalid Grid entered, pick a legal value')
    return False    

def printBoard():
    for meta_row in range(3):
        for mini_row in range(3):
            line = ''
            for meta_col in range(3):
                mini_board = full_board[meta_row][meta_col]
                cells = [c if c != '' else ' ' for c in mini_board[mini_row]]
                line += ' | '.join(cells)
                if meta_col < 2:
                    line += '  ||  '
            print(line)
        if meta_row < 2:
            print('-' * 35)
    print()

full_board = [[[[''] * 3 for _ in range(3)] for _ in range(3)] for _ in range(3)] 
meta_board = [[''] * 3 for _ in range(3)]
active_grid = None

isX = True

def play():

    global isX, active_grid

    sign = 'X' if isX else 'O'

    if not active_grid:
        grid_pos = input('Free move! \n Enter the grid square you want to play in  in row, col : ')
        grid_row, grid_col = grid_pos.split(',')
        grid_row, grid_col = int(grid_row), int(grid_col)
        active_grid = grid_row, grid_col

    else:
        grid_row, grid_col = active_grid

    
    if not isValidGrid(grid_row, grid_col):
        active_grid = None
        play()
        return 

    play_pos = input('Input your play position row, col : ')
    play_row, play_col = play_pos.split(',')
    play_row, play_col = int(play_row), int(play_col)

    if not isValidPlay(play_row, play_col, sign, full_board[grid_row][grid_col]):
        play()
        return 

    if checkWin(sign, full_board[grid_row][grid_col]):
        print('Mini_Board won')
        meta_board[grid_row][grid_col] = sign
    
    else:
        full = True
        for row in full_board[grid_row][grid_col]:
            if '' in row:
                full = False
        if full:
            meta_board[grid_row][grid_col] = 'D'
    
    if checkWin(sign, meta_board):
        print(f'{sign} is the winner')
        return 
    else:
        full = True
        for row in meta_board:
            if '' in row:
                full = False
        
        if full:
            print('It is a draw')
            return 

    
    if isValidGrid(play_row, play_col):
        active_grid = play_row, play_col
    else:
        active_grid = None

    

    
    
    isX = not isX

    printBoard()
    play()


play()


    


    
