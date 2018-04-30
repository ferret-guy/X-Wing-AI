import math

import pygame

from ship import Ship, Small_Ship, Movment


def rot_center(image, rect, angle):
	"""rotate an image while keeping its center"""
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = rot_image.get_rect(center=rect.center)
	return rot_image, rot_rect


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((500, 500))
	done = False
	is_blue = True
	x = 250
	y = 250
	scale = 1

	clock = pygame.time.Clock()
	x_wing = Small_Ship(x / scale, y / scale, 0)
	sprite = pygame.image.load("x-wing.gif")
	sprite_rect = sprite.get_rect()
	sprite_rect.centerx = 30
	sprite_rect.centery = 30

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					x_wing = Movment.straight_1(x_wing)
					print "Moved Up"
				elif event.key == pygame.K_DOWN:
					x_wing.t += math.pi / 2
					print "Moved Down"
				elif event.key == pygame.K_LEFT:
					x_wing = Movment.turn_3_left(x_wing)
					print "Moved Left"
				elif event.key == pygame.K_RIGHT:
					x_wing = Movment.turn_3_right(x_wing)
					print "Moved Right"
				else:
					print "Unknown key"

		screen.fill((0, 0, 0))
		if is_blue:
			color = (0, 128, 255)
		else:
			color = (255, 100, 0)

		rot_image = pygame.transform.rotate(sprite, -math.degrees(x_wing.t) - 90)
		rot_rect = rot_image.get_rect(center=sprite_rect.center)
		rot_rect.centerx, rot_rect.centery = int(x_wing.x * scale), int(x_wing.y * scale)
		screen.blit(rot_image, rot_rect)
		pygame.display.flip()
		clock.tick(60)
