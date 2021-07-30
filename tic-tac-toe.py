Create board
# %%
board = {'a': [0, 1, 2], 'b': [0, 1, 2], 'c': [0, 1, 2]}
def current_board(board):
    for row in board:
        print(row, board[row])

# %%
# INPUT Ask users to choose symbol
def user_symbol():
    user1 = input("User1 please choose your symbol, X or O: ")
    user2 = input("User2 please choose your symbol, X or O: ")
    if user1 == user2:
        user2 = input("Symbol already taken. Please choose another symbol!")
    return user1, user2
# %%

# OUTPUT Define which user starts first
import random
player1, player2 = user_symbol()
player_symbols = {0: player1, 1: player2}
current_player = random.randint(0, 1)
print(f"User with symbol {player_symbols[current_player]} starts first")
# %%
# INPUT Ask users in turns to input their position
def switch_player(current_player):
    if current_player == 0:
        current_player = 1
    elif current_player == 1:
        current_player = 0
    return current_player
# %%
def check_position(pos):
    
    if pos not in ['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']:
        print('Out of range')
        return False
        
    else:
        row = board[pos[0]]
        board_position = row[int(pos[1])] 
        if board_position in player_symbols.values():
            print('Position already taken')
            return False
    
        else:
            return True
# %%
def make_move(pos, current_player):
    
    row = board[pos[0]]
    
    row[int(pos[1])] = player_symbols[current_player]
   
    board[pos[0]]= row
    return board, current_player

# %%
def winner_takes_all(board, player_x):
    
    for r in board:
        row = board[r]
        
        if all(player_x == board_position for board_position in row):
            print(f'I hereby declare {player_x} as the winner')
            return True
    
    for col in [0, 1, 2]:
        if all(player_x == board[row][col] for row in board):
            print(f'I hereby declare {player_x} as the winner!!!')
            return True

    if all(player_x == board[row][col] for (row, col) in zip(board, [0, 1, 2])):
        print(f'I hereby declare {player_x} as the winner!!!')
        return True

    if all(player_x == board[row][col] for (row, col) in zip(board, [2, 1, 0])):
        print(f'I hereby declare {player_x} as the winner!!!')
        return True

    return False

current_board(board)

occupied_positions = 0

while True:
    # user1
    pos = input(f"Player {player_symbols[current_player]}, choose your position: ")
    if pos == 'q':
        break

    if check_position(pos):
        board, current_player = make_move(pos, current_player)

        if winner_takes_all(board, player_symbols[current_player]):
            answer = input(f' Does the loser want a rematch? y/n: ')
            if answer == 'y':
                occupied_positions = 0
                board = {'a': [0, 1, 2], 'b': [0, 1, 2], 'c': [0, 1, 2]}
                current_player = random.randint(0, 1)
                print(f"User with symbol {player_symbols[current_player]} starts first")
            else:
                print('Ciao bellas')
                break
        else:
            current_player = switch_player(current_player)
            occupied_positions+= 1
    
    if occupied_positions == 9:
        print('No winners here. Shame on you!!!')
        answer = input(f' Does the losers want a rematch? y/n: ')
        if answer == 'y':
            occupied_positions = 0
            board = {'a': [0, 1, 2], 'b': [0, 1, 2], 'c': [0, 1, 2]}
            current_player = random.randint(0, 1)
            print(f"User with symbol {player_symbols[current_player]} starts first")
        else:
            print('Ciao bellas')
            break
        
    print()

    current_board(board)
    
    

    # user2
    
# %%
    WHILE 
        IF Check if input from user is valid
        OUTPUT Display input on board
        IF Check if condition for win is fulfilled
            IF If yes, then userX is the winner
            IF If no, then keep playing
        IF Check if condition for a draw is fulfilled
            IF If yes, declare no winner
            INPUT Ask users for another round of the game