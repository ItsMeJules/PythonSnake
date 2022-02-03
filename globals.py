import yaml
import re

SCREEN_SIZE = (1000, 500)
GRID_SQUARE_SIZE = 30
SNAKE_COLOR = (224, 224, 224)
BG_COLOR = (0, 0, 0)

with open("config.yml") as stream:
	c = yaml.safe_load(stream)
	SCREEN_SIZE = c["window"]["width"], c["window"]["height"]
	GRID_SQUARE_SIZE = c["entity_size"]["snake_part"]
	SNAKE_COLOR = tuple(map(int, re.findall(r'\d+', c["colors"]["snake"])))
	BG_COLOR = tuple(map(int, re.findall(r'\d+', c["colors"]["background"])))
		