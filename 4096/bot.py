#!/usr/bin/env python3
import sys, socket, random

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

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(sys.argv[1])

# register name
s.send("example-bot\n".encode("utf-8"))
previous_score = 0

while True:
	board = read_board(s)

	direction = random.randint(1, 4)

	if direction == 1:
		up(s)
	elif direction == 2:
		down(s)
	elif direction == 3:
		left(s)
	else:
		right(s)