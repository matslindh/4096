import platform
import sys, socket

def read_board(s):
	board = []
	lines = s.recv(4096).decode("utf-8").split("\n")

	for line in lines:
		line = line.strip()

		if line.startswith("=="):
			return (board, int(line[3:]))

		if line.startswith("FIN"):
			print("Done: " + line[4:])
			sys.exit()

		board.append(line.split(" "))

	return board

def up(s):
	s.send("u\n".encode("utf-8"))

def down(s):
	s.send("d\n".encode("utf-8"))

def left(s):
	s.send("l\n".encode("utf-8"))

def right(s):
	s.send("r\n".encode("utf-8"))

def rotate_board(board, count):
    for c in range(0, count):
        rotated = [[0 for i in range(len(board))] for i in range(len(board[0]))]

        rows = len(board)

        for row_idx in range(0, rows):
            columns = len(board[row_idx])
            for el_idx in range(0, columns):
                rotated[columns - el_idx - 1][row_idx] = board[row_idx][el_idx]

        board = rotated

    return rotated

def merge_count(board):
	c = 0
	s = 0

	for x in range(0, len(board[0])):
		y = 0
		y_value = 0

		while y < len(board):
			if not board[y][x]:
				y += 1
				continue

			if not y_value:
				y_value = board[y][x]
				y += 1
				continue

			if y_value == board[y][x]:
				c += 1
				y += 1
				y_value = 0
				s += y_value * 2
			else:
				y_value = board[y][x]

			y += 1

	return (c, s)

def botsetup(name):
	if platform.system() == 'Windows':
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("127.0.0.1", 8765))
	else:
		s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		s.connect(sys.argv[1])

	# register name
	name += "\n"
	s.send(name.encode("utf-8"))

	return s
