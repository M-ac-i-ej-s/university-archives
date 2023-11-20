import sysv_ipc
import time

player = 1
game_counter = 0
game = '  ;  ;  '

key = 12
NULL_CHAR = '\0'

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
    for x in splitGame:
        print(x[0], ' ', x[1])


def check():
    splitGame = game.split(';')
    if(splitGame[game_counter][0] != ' ' and splitGame[game_counter][1] != ' '):
        if (splitGame[game_counter][0] == splitGame[game_counter][1]):
            return 'player 2 won'
        else:
            return 'player 1 won'


def make_move(letter: str, player: int, game_copy: str):
    splitGame = game_copy.split(';')
    splitGame[game_counter] = splitGame[game_counter][:player-1] + letter + splitGame[game_counter][player:]
    game_copy_2 = ''
    game_copy_2 += splitGame[0]
    for x in range(1):
        game_copy_2 += ';' + splitGame[x + 1]
    return game_copy_2


if player == 1:
    save_game(mem, game)
else:
    game_counter +=1    

while game_counter < 3:
    sem2.acquire()
    game = read_game(mem)

    print('Guess one of three letters A, B or C:')
    letter = str(input(f"Player {player}: "))

    while True:
        splitGame = game.split(';')
        if splitGame[game_counter][player-1] == ' ':
            game = make_move(letter, player, game)
            save_game(mem, game)
            break
        else:
            letter = str(input(f"Player {player}: "))
            game_counter += 1


    print(check())
    sem1.release()
    if game_counter == 3:
        break

    sem1.release()

try:
    sysv_ipc.remove_shared_memory(mem.id)
    sysv_ipc.remove_semaphore(sem1.id)
    sysv_ipc.remove_semaphore(sem2.id)
except sysv_ipc.ExistentialError:
    pass