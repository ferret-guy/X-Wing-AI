import math


class Point(object):
	def __init__(self, x, y, t):
		"""
		Point class, is a point
		:param x: x pos (normally in mm)
		:param y: y pos (normally in mm
		:param t: theta normally in rad
		"""
		self.x = x
		self.y = y
		self.t = t

	def dist(self, point):
		"""
		Caculates the distance to the selected point
		:param point: Another point
		:type point: Point
		:return: Distance
		:rtype: float
		"""
		return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

	def move_straight(self, len):
		self.x += len * math.cos(self.t)
		self.y += len * math.sin(self.t)
		return self


class Movment(object):
	@staticmethod
	def straight_1(curr_ship):
		"""
		Moves the ship 1 Straight
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		return curr_ship.move_straight(40)

	@staticmethod
	def straight_2(curr_ship):
		"""
		Moves the ship 2 Straight
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		return curr_ship.move_straight(80)

	@staticmethod
	def straight_3(curr_ship):
		"""
		Moves the ship 3 Straight
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		return curr_ship.move_straight(120)

	@staticmethod
	def straight_4(curr_ship):
		"""
		Moves the ship 4 Straight
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		return curr_ship.move_straight(160)

	@staticmethod
	def straight_5(curr_ship):
		"""
		Moves the ship 5 Straight
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		return curr_ship.move_straight(200)

	@staticmethod
	def curved_move(curr_ship, rad, ang, left):
		"""
		Moves the ship in a turn
		:param curr_ship: Current ship
		:type curr_ship: Ship
		:param rad: The radius in mm to move
		:type rad: int
		:param arc: angle to move (normally 45 deg or 90 deg in rad)
		:type arc: float
		:param bool left: true of left false otherwise
		:return: ship instance
		:rtype: Ship
		"""
		radius = rad
		arc_ang = ang
		if left:
			arc_ang = -arc_ang
		base_len, _ = curr_ship.base_size

		# Ghost point is used to propagate the maneuver TODO: Remove ghost point it can just be curr_ship
		ghost_point = Point(curr_ship.x, curr_ship.y, curr_ship.t)

		# Move foward half the base length to make the point inline with the start of the maneuver
		ghost_point = ghost_point.move_straight(base_len / 2)

		# Calculate the position of the point to rotate around
		if left:
			rot_point = Point(ghost_point.x, ghost_point.y, ghost_point.t - math.pi / 2)
		else:
			rot_point = Point(ghost_point.x, ghost_point.y, ghost_point.t + math.pi / 2)
		rot_point = rot_point.move_straight(radius)

		# Shift the rotation point to the origin them rotate the ghose point around it then move it back where we found it
		ghost_point.x, ghost_point.y = ghost_point.x - rot_point.x, ghost_point.y - rot_point.y
		ghost_point.x, ghost_point.y = ghost_point.x * math.cos(arc_ang) - ghost_point.y * math.sin(arc_ang), \
										ghost_point.x * math.sin(arc_ang) + ghost_point.y * math.cos(arc_ang)
		ghost_point.x, ghost_point.y = ghost_point.x + rot_point.x, ghost_point.y + rot_point.y

		# Move another half base length to make the virtual point at the same point as the center of the base
		ghost_point = ghost_point.move_straight(base_len / 2)

		# Update the looking vector
		if left:
			curr_ship.x, curr_ship.y, curr_ship.t = ghost_point.x, ghost_point.y, curr_ship.t + arc_ang
		else:
			curr_ship.x, curr_ship.y, curr_ship.t = ghost_point.x, ghost_point.y, curr_ship.t + arc_ang
		return curr_ship

	@staticmethod
	def turn_1_left(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 35
		arc_ang = math.pi / 2
		return Movment.curved_move(curr_ship, radius, arc_ang, True)

	@staticmethod
	def turn_1_right(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 35
		arc_ang = math.pi / 2
		return Movment.curved_move(curr_ship, radius, arc_ang, False)

	@staticmethod
	def turn_2_left(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 63
		arc_ang = math.pi / 2
		return Movment.curved_move(curr_ship, radius, arc_ang, True)

	@staticmethod
	def turn_2_right(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 63
		arc_ang = math.pi / 2
		return Movment.curved_move(curr_ship, radius, arc_ang, False)

	@staticmethod
	def turn_3_left(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 90
		arc_ang = math.pi / 2
		return Movment.curved_move(curr_ship, radius, arc_ang, True)

	@staticmethod
	def turn_3_right(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 90
		arc_ang = math.pi / 2
		return Movment.curved_move(curr_ship, radius, arc_ang, False)

	@staticmethod
	def bank_1_left(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 80
		arc_ang = math.pi / 4
		return Movment.curved_move(curr_ship, radius, arc_ang, True)

	@staticmethod
	def bank_1_right(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 80
		arc_ang = math.pi / 4
		return Movment.curved_move(curr_ship, radius, arc_ang, False)

	@staticmethod
	def bank_2_left(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 130
		arc_ang = math.pi / 4
		return Movment.curved_move(curr_ship, radius, arc_ang, True)

	@staticmethod
	def bank_2_right(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 130
		arc_ang = math.pi / 4
		return Movment.curved_move(curr_ship, radius, arc_ang, False)

	@staticmethod
	def bank_3_left(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 180
		arc_ang = math.pi / 4
		return Movment.curved_move(curr_ship, radius, arc_ang, True)

	@staticmethod
	def bank_3_right(curr_ship):
		"""
		:param Ship curr_ship: a ship instance
		:return: None
		"""
		radius = 180
		arc_ang = math.pi / 4
		return Movment.curved_move(curr_ship, radius, arc_ang, False)


class Ship(Point):
	def __init__(self, x, y, t):
		super(Ship, self).__init__(x, y, t)

	@property
	def base_size(self):
		"""
		Returns the size of the base in mm (width, Height
		:return: A tuple containing the Width and Height
		:rtype: tuple(int, int)
		"""
		raise NotImplementedError("Define the base size!")

	@property
	def name(self):
		"""
		The ships full name (e.g. Tie Fighter)
		:return: Ships name
		:rtype: str
		"""
		raise NotImplementedError("Implment the name!")


class Small_Ship(Ship):
	@property
	def base_size(self):
		"""
		Returns the size of the base in mm (width, Height
		:return: A tuple containing the Width and Height
		:rtype: tuple(int, int)
		"""
		return 34.2, 40

