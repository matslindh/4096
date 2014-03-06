import engine, sys, uuid, random

if len(sys.argv) < 2:
	sys.stderr.write("Usage: interface.py <randomseed>\n")
	sys.exit()

random.seed(sys.argv[1])

game = engine.Engine()
move_count = 0
game_name = sys.stdin.readline().strip()
identifier = str(uuid.uuid4())

sys.stderr.write("Game: " + game_name + "\n")
sys.stderr.write("Identifier: " + identifier + "\n")

game.print_board()

while True:
	c = sys.stdin.readline().strip()

	if c == 'u':
		game.up()
	elif c == 'd':
		game.down()
	elif c == 'l':
		game.left()
	elif c == 'r':
		game.right()

	game.print_board()

	move_count += 1

	if game.is_board_locked():
		break

sys.stderr.write("Score: " + str(game.score) + "\n")
sys.stderr.write("Moves: " + str(move_count) + "\n")