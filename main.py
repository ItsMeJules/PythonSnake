import sys
from turtle import bgcolor
import pygame

# My imports
from snake import *
from grid import Grid
from globals import *

pygame.init()

def game_loop(sk, gd, screen):
	screen.fill(BG_COLOR)
	pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(gd.getCenter(), (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE)))
	pygame.display.flip()

def main():
	screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)

	gd = Grid()
	sk = Snake([0, 0], [0, 1], 1)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		game_loop(sk, gd, screen)



if __name__ == "__main__":
	main()