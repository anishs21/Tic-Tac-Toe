import random

class TicTacToe:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.bot_X = 'X'
        self.bot_O = 'O'
        self.current_player = self.bot_X
        self.winner_combo = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

    def display_board(self):
        for i in range(3):
            row = ' | '.join(self.board[i*3:i*3+3])
            sep = "\n" + "- " * 5 + "\n" if i < 2 else "\n"
            print(row, end=sep)

    def get_possible_moves(self):
        return [i for i, v in enumerate(self.board) if v not in ['X', 'O']]

    def is_winner(self):
        for a, b, c in self.winner_combo:
            if self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if not self.get_possible_moves():
            return 'Tie'
        return None

    def best_move(self, symbol):
        # Try to win
        for move in self.get_possible_moves():
            self.board[move] = symbol
            if self.is_winner() == symbol:
                return move
            self.board[move] = str(move + 1)

        # Try to block opponent
        opponent = self.bot_X if symbol == self.bot_O else self.bot_O
        for move in self.get_possible_moves():
            self.board[move] = opponent
            if self.is_winner() == opponent:
                self.board[move] = str(move + 1)
                return move
            self.board[move] = str(move + 1)

        # Pick random
        return random.choice(self.get_possible_moves())

    def play(self):
        print("\nStarting Bot vs Bot Tic Tac Toe:\n")
        self.display_board()

        while True:
            move = self.best_move(self.current_player)
            self.board[move] = self.current_player
            print(f"\n{self.current_player} moved to position {move + 1}:\n")
            self.display_board()

            result = self.is_winner()
            if result:
                if result == 'Tie':
                    print("\nIt's a Tie!")
                else:
                    print(f"\nBot '{result}' wins!")
                break

            self.current_player = self.bot_O if self.current_player == self.bot_X else self.bot_X


if __name__ == "__main__":
    TicTacToe().play()
