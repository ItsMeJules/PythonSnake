import sys
from turtle import bgcolor
import numpy
import pygame

# My imports
from snake import Snake, SnakeDisplayer, Direction
from grid import Grid
from globals import *

pygame.init()

def main():
	gd = Grid(pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE))
	sk = Snake(numpy.array([3, 3]), Direction.EAST, 4)
	sd = SnakeDisplayer(sk)
	clock = pygame.time.Clock()

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
		clock.tick(10)
		sk.move(gd)
		sd.display(gd.screen)
		pygame.display.flip()
		gd.clearLastPos(sk)

if __name__ == "__main__":
	main()