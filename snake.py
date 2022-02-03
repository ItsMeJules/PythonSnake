from enum import Enum
from socket import gethostbyaddr
from typing import Tuple
import numpy as np
import pygame

from globals import *

class Direction(Enum):
	NORTH = 0
	SOUTH = 1
	WEST = 2
	EAST = 3

	@classmethod
	def fromMatrix(self, mt):
		if np.array_equal(mt, [0, -1]):
			return Direction.NORTH
		elif np.array_equal(mt, [0, 1]):
			return Direction.SOUTH
		elif np.array_equal(mt,[-1, 0]):
			return Direction.WEST
		elif np.array_equal(mt, [1, 0]):
			return Direction.EAST

class SnakePart:
	dirs = ([0, -1], #NORTH
		[0, 1], #SOUTH
		[-1, 0], #WEST
		[1, 0]) #EAST
			
	def __init__(self, pos, dir) -> None:
		self.__pos = pos
		self.__dir = dir

	def move(self, dir, grd) -> None:
		self.setPosition(np.add(self.__pos, dir), grd)

	def setPosition(self, pos, grd) -> None:
		if pos[0] < 0:
			pos[0] = grd.width
		elif pos[0] > grd.width:
			pos[0] = 0
		elif pos[1] < 0:
			pos[1] = grd.height
		elif pos[1] > grd.height:
			pos[1] = 0
		self.__pos = pos

	def getPosition(self, pixels = False) -> np.ndarray:
		if pixels:
			return np.multiply(self.__pos, GRID_SQUARE_SIZE)
		return self.__pos

	def setDirection(self, direction) -> bool:
		dir = SnakePart.dirs[direction.value]
		if not (-self.__dir[0] != dir[0] and -self.__dir[1] != dir[1]): #opposed directions
			return False
		self.__dir = dir

	def getDirection(self, pixels = False) -> np.ndarray:
		if pixels:
			return np.multiply(self.__dir, GRID_SQUARE_SIZE)
		return self.__dir
	
	def __str__(self) -> str:
		return f"x: {self.__pos[0]} y: {self.__pos[1]}"

class Snake:
	def __init__(self, pos, dir, len) -> None:
		self.len = len
		self.amountAppleAte = 0
		self.newDir = Direction.SOUTH
		self.__parts = [SnakePart(pos, dir)]

		for i in range(1, len):
			self.grow()

	def grow(self) -> None:
		last = self.__parts[-1]
		newPos = np.add(last.getPosition(), np.negative(last.getDirection()))
		newPart = SnakePart(newPos, last.getDirection())
		
		self.__parts.append(newPart)

	def move(self, grd) -> None:
		for i in range(len(self.__parts) - 1, 0, -1):
			previousPartDir = self.__parts[i if i == 0 else i - 1].getDirection()
			self.__parts[i].move(previousPartDir, grd)
			self.__parts[i].setDirection(Direction.fromMatrix(previousPartDir))

		head = self.getHead()
		head.setDirection(self.newDir)
		head.move(head.getDirection(), grd)

	def dir(self, dir) -> None:
		self.newDir = dir

	def getHead(self) -> SnakePart:
		return self.__parts[0]

	def getParts(self) -> np.ndarray:
		return self.__parts

	def __str__(self) -> str:
		return f"dirX: {self.__dir[0]} dirY: {self.__dir[1]} \
			len: {self.len}"

class SnakeDisplayer:
	def __init__(self, snake) -> None:
		self.__snake = snake

	def display(self, screen) -> None:
		for p in self.__snake.getParts():
			r = pygame.Rect(p.getPosition(True), (GRID_SQUARE_SIZE - 1, GRID_SQUARE_SIZE - 1))
			pygame.draw.rect(screen, SNAKE_COLOR, r)
	
