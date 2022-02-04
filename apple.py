import random

import pygame
import numpy as np

from globals import APPLE_COLOR, APPLE_SIZE, BG_COLOR, SNAKE_PART_SIZE
from snake import SnakePart

def display_apple(apl, screen):
	pygame.draw.circle(screen, APPLE_COLOR, apl.getPosition(True), APPLE_SIZE)

def clear_apple(apl, screen):
	pygame.draw.circle(screen, BG_COLOR, apl.getPosition(True), APPLE_SIZE)

class Apple:
	def __init__(self, gd, skParts) -> None:
		valid = False
		while not valid:
			pos = np.array([random.randrange(1, gd.width), random.randrange(1, gd.height)])
			valid = True
			for part in skParts:
				if np.array_equal(pos, np.add(part.getPosition(), 1)):
					valid = False
					break
		self.pos = pos
		self.eaten = False

	def spawn(self, gd, skParts) -> None:
		self.__init__(gd, skParts)

	def getPosition(self, pixels = False) -> np.ndarray:
		if pixels:
			return np.subtract(np.multiply(self.pos, SNAKE_PART_SIZE), SNAKE_PART_SIZE / 2)
		return self.pos