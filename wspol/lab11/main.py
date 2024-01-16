import threading
import os
import random

class Player:
    def __init__(self, name, board_size=10, treasure_path_length=30):
        self.name = name
        self.board_size = board_size
        self.treasure_path_length = treasure_path_length
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.opponent_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.treasure_position = None
        self.current_position = (0, 0)
        self.lock = threading.Lock()

    def generate_treasure_path(self):
        self.treasure_position = (random.randint(0, self.board_size-1), random.randint(0, self.board_size-1))
        x, y = self.treasure_position
        for _ in range(self.treasure_path_length):
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up' and y > 0:
                y -= 1
            elif direction == 'down' and y < self.board_size - 1:
                y += 1
            elif direction == 'left' and x > 0:
                x -= 1
            elif direction == 'right' and x < self.board_size - 1:
                x += 1
            self.board[y][x] = 'O'

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
        print(f"{self.name}'s Board:")
        for row in self.board:
            print(' '.join(row))
        print("\nOpponent's Board:")
        for row in self.opponent_board:
            print(' '.join(row))
        print("\nCurrent Position:", self.current_position)

    def move(self, direction):
        x, y = self.current_position
        if direction == 'up' and y > 0:
            y -= 1
        elif direction == 'down' and y < self.board_size - 1:
            y += 1
        elif direction == 'left' and x > 0:
            x -= 1
        elif direction == 'right' and x < self.board_size - 1:
            x += 1

        if self.board[y][x] == 'O':
            print(f"Congratulations! {self.name} found the treasure!")
            return True
        else:
            self.current_position = (x, y)
            return False

def play_game(player1, player2):
    current_player = random.choice([player1, player2])
    while True:
        with current_player.lock:
            current_player.print_board()
            move = input(f"{current_player.name}, enter your move (up/down/left/right): ").lower()
            if move in ['up', 'down', 'left', 'right']:
                if current_player.move(move):
                    print(f"{current_player.name} wins!")
                    break
            else:
                print("Invalid move! Please enter 'up', 'down', 'left', or 'right'.")
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")

    player1.generate_treasure_path()
    player2.generate_treasure_path()

    game_thread = threading.Thread(target=play_game, args=(player1, player2))
    game_thread.start()
    game_thread.join()