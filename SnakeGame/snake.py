import random
import curses

#Initialize Screen
s = curses.initscr()
curses.start_color()
curses.curs_set(0)

curses.color_content(10)
sh, sw = s.getmaxyx()
#creating window
win = curses.newwin(sh, sw, 0, 0)
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
#keypad Input
win.keypad(1)
win.timeout(100)#refresh screen

#snake starting codinates
snake_x = sw//4
snake_y = sh//2

#snake bodyPart
snake = [
	[snake_y, snake_x],
	[snake_y, snake_x - 1],
	[snake_y, snake_x - 2]
]

#food
food = [sh//2, sw//2]
win.addch(food[0], food[1], curses.ACS_BLOCK)

#Initial Direction
key = curses.KEY_RIGHT

while True:
	next_key = win.getch()
	key = key if next_key == -1 else next_key
	#Check game is over or not
	if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	#new head
	new_head = [snake[0][0], snake[0][1]]

	#CHECK THE NEW DIRECTION
	if key == curses.KEY_DOWN:
		new_head[0] +=1
	if key == curses.KEY_UP:
		new_head[0] -=1
	if key == curses.KEY_LEFT:
		new_head[1] -=1
	if key == curses.KEY_RIGHT:
		new_head[1] +=1

	#insert new head
	snake.insert(0, new_head)

	#whether snake eat food and create new food
	if snake[0] == food:
		food = None
		while food is None:
			new_food = [
						random.randint(1, sh - 1),
						random.randint(1, sw - 1)
			]
			food = new_food if new_food not in snake else None
		#add the new food
		win.addch(food[0], food[1], curses.ACS_BLOCK)
	else:
		tail = snake.pop()
		win.addch(tail[0], tail[1], ' ')
	
	win.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND,curses.A_BOLD)