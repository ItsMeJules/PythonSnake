from typing import Tuple
import pygame

from snake import Snake
from globals import *

class Grid:
	def __init__(self) -> None:
		self.width = SCREEN_SIZE[0] / GRID_SQUARE_SIZE
		self.height = SCREEN_SIZE[1] / GRID_SQUARE_SIZE
	
	def getCenter(self, offset = 0) -> Tuple[int, int]:
		return self.width / 2 * (GRID_SQUARE_SIZE) - offset, \
				self.height / 2 * (GRID_SQUARE_SIZE) - offset
	
	def clearLastPos(self, sk) -> None:
		sk.getPos()[]
