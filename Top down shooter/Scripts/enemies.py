import pygame
from math import floor
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


class MeleeEnemy: 
	def __init__(self, startingPosition):
		self.pos = startingPosition
		self.direction = pygame.math.Vector2(1, 0)
		
		self.moveSpeed = 2
		self.movingTo = None

		self.isIdle = False
		self.isAttacking = False

		self.animationDelayFrame = 0
		self.animationFrame = 0
		self.currentSprite = None
		self.facing = None
	
	def drawEnemy(self, surface, sprites):
		if (not self.isIdle):
			if (self.animationDelayFrame % 4 == 0):
				self.animationFrame += 1

			if (self.animationFrame >= len(sprites["walk-"+self.facing])):
				self.animationFrame = 0
			
			self.currentSprite = sprites["walk-"+self.facing][self.animationFrame]
			self.animationDelayFrame += 1			
		elif (self.isIdle):
			self.animationFrame = 0
			self.currentSprite = sprites["walk-"+self.facing][self.animationFrame]

		surface.blit(self.currentSprite, (self.pos.x, self.pos.y, self.currentSprite.get_rect().x, self.currentSprite.get_rect().y))


	def findOptimalPath(self, targetPos, matrix, tileSize):
		grid = Grid(matrix=matrix)

		start = grid.node(floor(self.pos.x / tileSize), floor(self.pos.y / tileSize))
		end = grid.node(floor(targetPos.x / tileSize), floor(targetPos.y / tileSize))

		finder = DijkstraFinder(diagonal_movement=DiagonalMovement.always)
		path, runs = finder.find_path(start, end, grid)

		# print('operations:', runs, 'path length:', len(path))
		# print(grid.grid_str(path=path, start=start, end=end))
		# print(path, floor(self.pos.x / tileSize), floor(self.pos.y / tileSize))
		if (len(path) == 2):
			self.isIdle = True
			self.movingTo = None
		else:
			self.isIdle = False
			self.movingTo = pygame.math.Vector2((path[1][0] * tileSize) + tileSize/2, (path[1][1] * tileSize) + tileSize/2)

	def moveToTarget(self, targetPos, matrix, tileSize):
		d = 10000
		if (self.movingTo != None):
			d = self.pos.distance_to(self.movingTo)

		if (d < 2 or self.movingTo == None):
			self.findOptimalPath(targetPos, matrix, tileSize)
		
		if (self.isIdle == False):
			print("----------")
			print(d)
			print(self.pos, self.movingTo)
			if (self.movingTo.x < self.pos.x): 
				self.direction.x = -1
			elif (self.movingTo.x > self.pos.x): 
				self.direction.x = 1
			else: 
				self.direction.x = 0
			if (self.movingTo.y < self.pos.y): 
				self.direction.y = -1
			elif (self.movingTo.y > self.pos.y): 
				self.direction.y = 1
			else:
				self.direction.y = 0

			print(self.direction)
			print("----------")
			diagonal = 1
			if (self.direction.x != 0 and self.direction.y != 0):
				diagonal = 0.707106

			# print(self.direction, self.moveSpeed, diagonal, self.direction * self.moveSpeed * diagonal)
			self.pos += self.direction * self.moveSpeed * diagonal

		self.determineFacing()



	def determineFacing(self):
		if (self.direction.x < 0):
			self.facing = "left"
		elif (self.direction.y < 0):
			self.facing = "up"
		elif (self.direction.y > 0):
			self.facing = "down"
		elif (self.direction.x > 0):
			self.facing = "right"


class RangedEnemy: 
	def __init__(self, startingPosition):
		self.pos = startingPosition
		self.direction = pygame.math.Vector2(0, 1)
		
		self.currentAnimation = None





# matrix = [
#   [1, 1, 1, 1, 0, 1, 1],
#   [1, 0, 1, 1, 1, 1, 1],
#   [1, 1, 1, 1, 1, 1, 1]
# ]
# grid = Grid(matrix=matrix)

# start = grid.node(0, 0)
# end = grid.node(6, 2)

# finder1 = AStarFinder(diagonal_movement=DiagonalMovement.always)
# path, runs = finder1.find_path(start, end, grid)

# grid.cleanup()

# finder2 = DijkstraFinder(diagonal_movement=DiagonalMovement.always)
# path2, run2, = finder2.find_path(start, end, grid)

# print('operations:', runs, 'path length:', len(path))
# print(grid.grid_str(path=path, start=start, end=end))

# print('operations:', run2, 'path length:', len(path2))
# print(grid.grid_str(path=path2, start=start, end=end))

# print(path, path2)