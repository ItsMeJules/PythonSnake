from typing import Tuple
import pygame

from snake import SnakePart
from globals import *

class Grid:
	def __init__(self, screen) -> None:
		self.screen = screen
		self.width = SCREEN_SIZE[0] / GRID_SQUARE_SIZE
		self.height = SCREEN_SIZE[1] / GRID_SQUARE_SIZE
	
	def getCenter(self, offset = 0) -> Tuple[int, int]:
		return self.width / 2 * (GRID_SQUARE_SIZE) - offset, \
				self.height / 2 * (GRID_SQUARE_SIZE) - offset
	
	def clearLastPos(self, sk) -> None:
		for p in sk.getParts():
			pygame.draw.rect(self.screen, BG_COLOR, pygame.Rect(p.getPosition(True), (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE)))