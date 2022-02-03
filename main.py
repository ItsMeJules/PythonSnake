import sys
from turtle import bgcolor
import pygame

# My imports
from snake import Snake, SnakeDisplayer
from grid import Grid
from globals import *

pygame.init()

def game_loop(sd, gd):
	sd.display(gd.screen)
	pygame.display.flip()

def main():
	gd = Grid(pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE))
	sk = Snake([3, 3], [0, 1], 2)
	sd = SnakeDisplayer(sk)

	gd.screen.fill(BG_COLOR)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		game_loop(sd, gd)



if __name__ == "__main__":
	main()