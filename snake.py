from enum import Enum
from typing import Tuple
import numpy as np
import pygame

from globals import *

class Direction(Enum):
	NORTH = 0
	SOUTH = 1
	WEST = 2
	EAST = 3

class SnakePart:
	def __init__(self, pos) -> None:
		self.__pos = pos

	def getPosition(self, pixels = False) -> Tuple[int, int]:
		if pixels:
			return np.multiply(self.__pos, GRID_SQUARE_SIZE)
		return self.__pos
	
	def __str__(self) -> str:
		return f"x: {self.__pos[0]} y: {self.__pos[1]}"

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
		self.parts = [SnakePart(pos)]
		for i in range(1, len):
			self.grow()

	def grow(self) -> None:
		newPos = np.add(self.parts[-1].getPosition(), np.negative(self.__dir))
		newPart = SnakePart(newPos)
		self.parts.append(newPart)
	
	def __isDirectionValid(self, direction) -> bool:
		return (-self.__dir[0] != direction[0]
			and -self.__dir[1] != direction[1])

	def setPosition(self, pos, grd) -> None:
		if pos[0] < 0:
			pos[0] = grd.width
		elif pos[0] > grd.width:
			pos[0] = 0
		elif pos[1] < 0:
			pos[1] = grd.height
		elif pos[1] > grd.height:
			pos[1] = 0

	def getPosition(self, pixels = False) -> Tuple[int, int]:
		if pixels:
			return np.multiply(self.__pos, GRID_SQUARE_SIZE)
		return self.__pos
	
	def setDirection(self, direction) -> bool:
		if not self.__isDirectionValid(Snake.dirs[direction]):
			return False
		self.__dir = Snake.dirs[direction]
	
	def getDirection(self) -> Tuple[int, int]:
		return self.__dir

	def __str__(self) -> str:
		return f"posX: {self.pos[0]} posY: {self.pos[1]} \
			dirX: {self.__dir[0]} dirY: {self.__dir[1]} \
			len: {self.len}"

class SnakeDisplayer:
	def __init__(self, snake) -> None:
		self.__snake = snake

	def display(self, screen) -> None:
		for p in self.__snake.parts:
			r = pygame.Rect(p.getPosition(True), (GRID_SQUARE_SIZE - 1, GRID_SQUARE_SIZE - 1))
			pygame.draw.rect(screen, SNAKE_COLOR, r)
	
