from enum import Enum

class Direction(Enum):
	NORTH = 0
	SOUTH = 1
	WEST = 2
	EAST = 3

class Snake:
	dirs = ([0, -1], #NORTH
			[0, 1], #SOUTH
			[-1, 0], #WEST
			[1, 0]) #EAST

	def __init__(self, pos, dir, len) -> None:
		self.__pos = pos
		self.__dir = dir
		self.len = len
		self.amountAppleAte = 0

	def __isDirectionValid(self, direction) -> bool:
		return (-self.dir[0] != direction[0]
			and -self.dir[1] != direction[1])

	def setPosition(self, pos, screen):
		if pos[0] < 0:
			pos[0] = screen.get_width()
		elif pos[0] > screen.get_width():
			pos[0] = 0
		elif pos[1] < 0:
			pos[1] = screen.get_height()
		elif pos[1] > screen.get_height():
			pos[1] = 0
	
	def setDirection(self, direction) -> bool:
		if not self.__isDirectionValid(Snake.dirs[direction]):
			return False
		self.dir = Snake.dirs[direction]

	def __str__(self) -> str:
		return f"posX: {self.pos[0]} posY: {self.pos[1]} \
			dirX: {self.dir[0]} dirY: {self.dir[1]} \
			len: {self.len}"