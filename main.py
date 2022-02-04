#!/usr/bin/env python3

import sys
import numpy
import pygame
import random
from datetime import datetime

# My imports
from snake import *
from grid import *
from globals import *
from apple import *

pygame.init()

def main():
	gd = Grid(pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE))
	sk = Snake(numpy.array([3, 3]), Direction.EAST, 4)
	clock = pygame.time.Clock()
	apl = Apple(gd)
	random.seed(datetime.now())

	pygame.display.set_caption("Snake.py")
	gd.screen.fill(BG_COLOR)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					sk.dir(Direction.NORTH)
				elif event.key == pygame.K_DOWN:
					sk.dir(Direction.SOUTH)
				elif event.key == pygame.K_LEFT:
					sk.dir(Direction.WEST)
				elif event.key == pygame.K_RIGHT:
					sk.dir(Direction.EAST)
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
		sk.move(gd)
		if sk.canEat(apl):
			sk.grow()
			clear_apple(apl, gd.screen)
			apl.spawn(gd)
		walks_on_itself(sk)
		display_snake(sk, gd.screen)
		display_apple(apl, gd.screen)
		pygame.display.flip()
		gd.clearLastPos(sk)
		clock.tick(10)

if __name__ == "__main__":
	main()