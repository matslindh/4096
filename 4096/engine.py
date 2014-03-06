import random

class Engine:
    def __init__(self):
        self.board = [[0 for i in range(4)] for i in range(4)]
        self.score = 0
        self.add_random_block()
        self.add_random_block()

    def left(self):
        self.next(1)

    def right(self):
        self.next(3)

    def up(self):
        self.next(2)

    def down(self):
        self.next()

    def rotate_board(self, board, count):
        for c in range(0, count):
            rotated = [[0 for i in range(len(board))] for i in range(len(board[0]))]

            rows = len(board)

            for row_idx in range(0, rows):
                columns = len(board[row_idx])
                for el_idx in range(0, columns):
                    rotated[columns - el_idx - 1][row_idx] = board[row_idx][el_idx]

            board = rotated

        return rotated

    def next(self, rotate_count = 0):
        board = self.board
        
        if rotate_count:
            board = self.rotate_board(board, rotate_count)

        merged = [[0 for i in range(len(board[0]))] for i in range(len(board))]

        for row_idx in range(0, len(board) - 1):
            for el_idx in range(0, len(board[row_idx])):
                if merged[row_idx][el_idx]:
                    continue

                current_cell = board[row_idx][el_idx]
                next_cell = board[row_idx+1][el_idx]

                if not current_cell:
                    continue

                if current_cell == next_cell:
                    board[row_idx+1][el_idx] *= 2
                    board[row_idx][el_idx] = 0
                    merged[row_idx+1][el_idx] = 1
                    self.score += self.score_bonus_value(current_cell)
                elif not next_cell:
                    board[row_idx+1][el_idx] = current_cell
                    board[row_idx][el_idx] = 0

        if rotate_count:
            board = self.rotate_board(board, 4 - rotate_count)

        self.board = board
        self.add_random_block()

    def add_random_block(self, val=None):
        avail = self.available_spots()

        if avail:
            (row, column) = avail[random.randint(0, len(avail) - 1)]

            self.board[row][column] = 4 if random.randint(0,8) == 8 else 2
            self.score += self.board[row][column]

    def available_spots(self):
        spots = []

        for (row_idx, row) in enumerate(self.board):
            for (el_idx, el) in enumerate(row):
                if el == 0:
                    spots.append((row_idx, el_idx))

        return spots

    def is_board_locked(self):
        if self.available_spots():
            return False

        board = self.board

        for row_idx in range(0, len(board) - 1):
            for el_idx in range(0, len(board[row_idx])):
                if board[row_idx][el_idx] == board[row_idx+1][el_idx]:
                    return False

        for row_idx in range(0, len(board)):
            for el_idx in range(0, len(board[row_idx]) - 1):
                if board[row_idx][el_idx] == board[row_idx][el_idx+1]:
                    return False

        return True

    def score_bonus_value(self, val):
        score = {
            2: 2, 
            4: 5, 
            8: 10, 
            16: 25, 
            32: 50, 
            64: 125, 
            128: 250, 
            256: 500, 
            512: 1000, 
            1024: 2000, 
            2048: 4000, 
            4096: 8000,
            8192: 16000,
            16384: 32500,
        }

        if val in score:
            return score[val]

        # too high, lets just .. be happy for them.
        return val*2

    def to_string(self):
        s = ""

        for row in self.board:
            s += ' '.join(map(str, row)) + "\n"

        s += "== " + str(self.score) + "\n"

        return s  


"""eng = Engine()
eng.add_random_block()
eng.add_random_block()
eng.print_board()

while True:
    key = input('u / d / l / r: ').strip()

    if key == 'u':
        eng.up()
    elif key == 'd':
        eng.down()
    elif key == 'l':
        eng.left()
    elif key == 'r':
        eng.right()
    else:
        continue

    eng.print_board()
    """