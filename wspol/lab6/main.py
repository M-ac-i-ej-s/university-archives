import sysv_ipc
import time

player = 1
game_counter = 2
move_counter = 0
game = '  ;  ;  '

key = 12
NULL_CHAR = '\0'

player_1_win = 0
player_2_win = 0

try:
    sem1 = sysv_ipc.Semaphore(key, sysv_ipc.IPC_CREX, 0o700, 0)
    sem2 = sysv_ipc.Semaphore(key + 1, sysv_ipc.IPC_CREX, 0o700, 1)
    mem = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREX)
    player = 1
except sysv_ipc.ExistentialError:
    sem1 = sysv_ipc.Semaphore(key + 1)
    sem2 = sysv_ipc.Semaphore(key)
    mem = sysv_ipc.SharedMemory(key)
    player = 2
    time.sleep(0.1)


def read_game(mem):
    s = mem.read()
    s = s.decode()
    i = s.find(NULL_CHAR)
    if i != -1:
        s = s[:i]
    return s


def save_game(mem, s):
    s += NULL_CHAR
    s = s.encode()
    mem.write(s)


def print_game():
    splitGame = game.split(';')
    print(splitGame[game_counter+1])


def check(game_number):
    splitGame = game.split(';')
    if(splitGame[game_number][0] != ' ' and splitGame[game_number][1] != ' '):
        if (splitGame[game_number][0] == splitGame[game_number][1]):
            return 'player 2 won this round'
        else:
            return 'player 1 won this round'   


def make_move(letter: str, player: int, game_copy: str):
    splitGame = game_copy.split(';')
    splitGame[game_counter] = splitGame[game_counter][:player-1] + letter + splitGame[game_counter][player:]
    game_copy_2 = ''
    game_copy_2 += splitGame[0]
    for x in range(len(splitGame)-1):
        game_copy_2 += ';' + splitGame[x + 1]
    return game_copy_2

def printFinalWin():
    if(player_1_win > player_2_win):
        print('Player 1 won the game !!!')
    else: 
        print('Player 2 won the game !!!')    

if player == 1:
    save_game(mem, game) 

while game_counter >= -1:
    try:
        sem2.acquire()
    except:
        printFinalWin()
        print('end')
        break    
    game = read_game(mem)

    if(game_counter != 2 and player == 1):
        if(check(game_counter+1) == 'player 2 won this round'):
            player_2_win += 1
        else:
            player_1_win += 1    
        print(check(game_counter+1))

    if(game_counter == -1):
        printFinalWin()
        print('end')
        break

    print('Guess one of three letters A, B or C:')
    letter = str(input(f"Player {player}: "))

    game = read_game(mem)
    game = make_move(letter, player, game)
    save_game(mem, game)

    if(player == 2):
        if(check(game_counter) == 'player 2 won this round'):
            player_2_win += 1
        else:
            player_1_win += 1 
        print(check(game_counter))

    game_counter -=1

    print_game()

    try:
        sem1.release()
    except:
        printFinalWin()
        print('end')
        break    

try:
    sysv_ipc.remove_shared_memory(mem.id)
    sysv_ipc.remove_semaphore(sem1.id)
    sysv_ipc.remove_semaphore(sem2.id)
except sysv_ipc.ExistentialError:
    pass