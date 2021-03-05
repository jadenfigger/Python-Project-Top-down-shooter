import pygame
from math import floor, atan2, pi, cos, sin
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


frameCount = 0

class Enemy: 
	def __init__(self):
		self.pos = None
		self.direction = pygame.math.Vector2(1, 0)
		self.enemyWidHei = (48, 67)
		
		self.attackDelay = 60
		self.startOfDelay = -60

		self.maxHealth = 100
		self.currentHealth = self.maxHealth
		self.attackDamage = 5

		self.moveSpeed = 2
		self.movingTo = None

		self.isIdle = False
		self.isAttacking = False
		self.dealDamage = False
		self.atNeighboringTile = False

		self.attackingRadius = [40, 45]

		self.animationDelayFrame = 0
		self.animationFrame = 0
		self.currentSprite = None
		self.currentAttackSprite = None
		self.facing = None

		
		self.skeletonEnemySprites = {"walk-up": [], "walk-left": [], "walk-down": [], "walk-right": [],
                                  "attack-up": [], "attack-left": [], "attack-down": [], "attack-right": [],
                                  "dying": []}
		self.bowedEnemySprites = {"walk-up": [], "walk-left": [], "walk-down": [], "walk-right": [],
                                  "attack-up": [], "attack-left": [], "attack-down": [], "attack-right": [],
                                  "dying": []}
		self.longswordSprites = {"sword-up": [], "sword-left": [], "sword-down": [], "sword-right": []}

		self.createEnemySprites()

	def createEnemySprites(self):
		meleeSkeletonSheet = pygame.image.load("Characters/Enemies/MeleeThief.png").convert_alpha()
		bowedSpriteSheet = pygame.image.load("Characters/Enemies/MeleeSkeleton.png").convert_alpha()
		longswordSpriteSheet = pygame.image.load("Characters/Enemies/WEAPON_longsword.png").convert_alpha()

		directions = ["up", "left", "down", "right"]

		count = 0
		for direction in directions:
			# Walking
			for i in range(9):
				self.skeletonEnemySprites["walk-"+direction].append(pygame.transform.scale(meleeSkeletonSheet.subsurface((64 * i + 13, 525 + (count * 64), 36, 50)), self.enemyWidHei))
				self.bowedEnemySprites["walk-"+direction].append(pygame.transform.scale(bowedSpriteSheet.subsurface((64 * i + 13, 525 + (count * 64), 36, 50)), self.enemyWidHei))
			# Longsword Sword
			for i in range(6):
				self.longswordSprites["sword-"+direction].append(longswordSpriteSheet.subsurface((192*i, count * 192, 192, 192)))
			# Attacking for bowed
			for i in range(13):
				self.bowedEnemySprites["attack-"+direction].append(pygame.transform.scale(bowedSpriteSheet.subsurface((64 * i + 13, 1038 + ((count) * 64), 36, 50)), self.enemyWidHei))  
			# Attacking for melee skeleton
			for i in range(6):
				self.skeletonEnemySprites["attack-"+direction].append(pygame.transform.scale(meleeSkeletonSheet.subsurface((64 * i + 13, 781 + ((count)* 64), 36, 50)), self.enemyWidHei))
			count += 1
	
			# Dying
			for i in range(6):
				self.skeletonEnemySprites["dying"].append(pygame.transform.scale(meleeSkeletonSheet.subsurface((64 * i + 13, 1292, 36, 50)), self.enemyWidHei))
				self.bowedEnemySprites["dying"].append(pygame.transform.scale(bowedSpriteSheet.subsurface((64 * i + 13, 1292, 36, 50)), self.enemyWidHei)) 


	def findOptimalPath(self, targetPos, matrix, tileSize):
		grid = Grid(matrix=matrix)

		start = grid.node(floor(self.pos.x / tileSize), floor(self.pos.y / tileSize))
		end = grid.node(floor(targetPos.x / tileSize), floor(targetPos.y / tileSize))

		finder = DijkstraFinder(diagonal_movement=DiagonalMovement.always)
		path, runs = finder.find_path(start, end, grid)

		if (len(path) <= 3):
			self.atNeighboringTile = True
			self.isAttacking = True
			self.animationDelayFrame = 0
			self.animationFrame = 0
		else:
			# self.animationDelayFrame = 0
			# self.animationFrame = 0
			self.isAttacking = False
			self.isIdle = False
			self.atNeighboringTile = False
			self.movingTo = pygame.math.Vector2((path[1][0] * tileSize) + tileSize/2, (path[1][1] * tileSize) + tileSize/2)

	def moveToTarget(self, targetPos, matrix, tileSize):
		if (self.atNeighboringTile):
			dx = float(self.pos.x + self.enemyWidHei[0]/2) - targetPos.x
			dy = float(self.pos.y + self.enemyWidHei[1]/2) - (targetPos.y)
			rads = atan2(-dy, dx)
			rads %= 2*pi

			self.movingTo = pygame.math.Vector2(round(targetPos.x + (cos(rads) * self.attackingRadius[0])), round(targetPos.y + (sin(rads) * self.attackingRadius[0])))

		if (self.movingTo == None or self.isIdle == False):
			self.findOptimalPath(targetPos, matrix, tileSize)
		
		if (self.isIdle == False):
			self.isAttacking = False
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

			diagonal = 1
			if (self.direction.x != 0 and self.direction.y != 0):
				diagonal = 0.717106

			self.pos += self.direction * self.moveSpeed * diagonal
			self.pos.x = round(self.pos.x)
			self.pos.y = round(self.pos.y)

		if (self.pos.distance_to(targetPos) < self.attackingRadius[1]):
			self.isAttacking = True
			self.movingTo = None
			self.isIdle = True
		else:
			# self.animationDelayFrame = 0
			# self.animationFrame = 0
			self.isAttacking = False
			self.isIdle = False

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


class MeleeSkeletonEnemy(Enemy): 
	def __init__(self, startingPosition):
		super().__init__()
		self.pos = startingPosition

	def drawEnemy(self, surface, targetPos):
		global frameCount
		frameCount += 1
		if (self.isAttacking and self.isIdle):
			if (self.animationDelayFrame % 7 == 0):
				self.animationFrame += 1

			if (self.animationFrame >= len(self.skeletonEnemySprites["attack-"+self.facing])):
				self.animationFrame = 0

			if (self.animationFrame == 4 and self.attackDelay + self.startOfDelay > frameCount):
				self.startOfDelay = frameCount
				self.dealDamage = True
			else:
				self.dealDamage = False
			
			self.currentSprite = self.skeletonEnemySprites["attack-"+self.facing][self.animationFrame]
			self.currentAttackSprite = self.longswordSprites["sword-"+self.facing][self.animationFrame]
			self.animationDelayFrame += 1	
		elif (not self.isIdle):
			if (self.animationDelayFrame % 4 == 0):
				self.animationFrame += 1

			if (self.animationFrame >= len(self.skeletonEnemySprites["walk-"+self.facing])):
				self.animationFrame = 0
			
			self.currentSprite = self.skeletonEnemySprites["walk-"+self.facing][self.animationFrame]
			self.animationDelayFrame += 1			
		elif (self.isIdle):
			self.animationFrame = 0
			self.currentSprite = self.skeletonEnemySprites["walk-"+self.facing][self.animationFrame]

		surface.blit(self.currentSprite, (self.pos.x, self.pos.y, self.currentSprite.get_rect().x, self.currentSprite.get_rect().y))
		        if (self.isAttacking):
            surface.blit(self.currentAttackSprite, (
                self.pos.x - (self.currentAttackSprite.get_size()[0] / 3) - 6,
                self.pos.y - (self.currentAttackSprite.get_size()[1] / 3) - 3,
                self.currentAttackSprite.get_rect().x, self.currentAttackSprite.get_rect().y))

		sHeathBarBack = pygame.Surface((int(self.enemyWidHei[0]), 10))
		sHeathBarBack.set_alpha(100)
		sHeathBarBack.fill((0, 0, 0))
		surface.blit(sHeathBarBack, (self.pos.x, self.pos.y - 10))
		pygame.draw.rect(surface, (255, 0, 0), (self.pos.x, self.pos.y-10, int((48 * self.currentHealth/self.maxHealth)), 10))


		# swordTranslations = {"up": [-86, 80], "left": [7, 2], "down": [4, 7], "right": [-7, 4]}
		# surface.blit(self.skeletonEnemySprites["attack-up"][5], (48, 48))
		# surface.blit(self.longswordSprites["sword-up"][5], (48+swordTranslations["up"][0], 48+swordTranslations["up"][1]))
		# print((48+swordTranslations["up"][0], 48+swordTranslations["up"][1]))
		# directions = ["up", "left", "down", "right"]
		# count = 0
		# for d in directions:
		# 	for i in range(6):
		# 		surface.blit(self.skeletonEnemySprites["attack-"+d][i], (16 + (64 * i), 32 + (64 * count), 
		# 					 self.skeletonEnemySprites["attack-"+d][i].get_rect().x, self.skeletonEnemySprites["attack-"+d][i].get_rect().y))
		# 		surface.blit(self.longswordSprites["sword-"+d][i], ((16 + (64 * i)) - 30, (32 + (64 * count) - 30)))

		# 	count += 1







