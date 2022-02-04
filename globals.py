import yaml
import re

SCREEN_SIZE = (1000, 500)
SNAKE_PART_SIZE = 30
APPLE_SIZE = 15

SNAKE_COLOR = (224, 224, 224)
APPLE_COLOR = (255, 255, 0)
BG_COLOR = (0, 0, 0)

with open("config.yml") as stream:
	c = yaml.safe_load(stream)
	SCREEN_SIZE = c["window"]["width"], c["window"]["height"]
	SNAKE_PART_SIZE = c["entity_size"]["snake_part"]
	APPLE_SIZE = c["entity_size"]["apple"]

	SNAKE_COLOR = tuple(map(int, re.findall(r'\d+', c["colors"]["snake"])))
	APPLE_COLOR = tuple(map(int, re.findall(r'\d+', c["colors"]["apple"])))
	BG_COLOR = tuple(map(int, re.findall(r'\d+', c["colors"]["background"])))
		