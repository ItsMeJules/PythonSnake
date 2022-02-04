from typing import Tuple
import pygame

# from snake import SnakePart
from globals import *

class Grid:
	def __init__(self, screen) -> None:
		self.screen = screen
		self.width = int(SCREEN_SIZE[0] / SNAKE_PART_SIZE)
		self.height = int(SCREEN_SIZE[1] / SNAKE_PART_SIZE)
	
	def getCenter(self, offset = 0) -> Tuple[int, int]:
		return self.width / 2 * (SNAKE_PART_SIZE) - offset, \
				self.height / 2 * (SNAKE_PART_SIZE) - offset
	
	def clearLastPos(self, sk) -> None:
		for p in sk.getParts():
			pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(p.getPosition(True), (SNAKE_PART_SIZE, SNAKE_PART_SIZE)))