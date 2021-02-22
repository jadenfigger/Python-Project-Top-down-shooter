import pygame
import sys

WIDTH, HEIGHT = SCREEN_SIZE = (1024, 768)
GAME_FPS = 60



tiles = [[0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0]]


class Player:
	def __init__(self):
		self.direction = pygame.math.Vector2(0, 1)
		self.playerWidHei = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
		self.vel = pygame.math.Vector2(0, 0)
		self.acc = pygame.math.Vector2(0, 0)
		self.moveSpeed = 3
		self.maxSpeed = 10
		self.rotationAngle = 0
		self.rotationSpeed = 1

		self.isIdle = True

		self.path = "Characters/"
		self.sprites = {"idle": [None] * 4, "up": [None] * 8, "down": [None] * 8, "right": [None] * 8, "left": [None] * 8}
		self.walkingSpriteSheet = pygame.image.load("Characters/BODY_male_walking.png")

	def createSprites(self):
		# x: 16 y: 14, x: 49 y: 63  xWidth = 33 yHeight = 49  yBuffer = 15
		for i in range(4):
			self.sprites["idle"][i] = self.walkingSpriteSheet.subsurface((16, 14 + (i * 64), 33, 49))
		self.playerWidHei = pygame.math.Vector2(self.sprites["idle"][i].get_size())


	def drawPlayer(self, surface):
		# if (self.isIdle):
		if (self.direction == (0, -1)):
			surface.blit(self.sprites["idle"][0], (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))
		elif (self.direction == (-1, 0)):
			surface.blit(self.sprites["idle"][1], (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))
		elif (self.direction == (0, 1)):
			surface.blit(self.sprites["idle"][2], (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))
		elif (self.direction == (1, 0)):
			surface.blit(self.sprites["idle"][3], (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))


	def move(self): 
		if (not self.isIdle):
			self.pos += self.direction * self.moveSpeed


class Ground:
	def __init__(self):
		self.tiles = {"darkGrass": "darkGrass1.png", "dirt": "dirt1.png", "grass": "grass1.png", 
						  "road": "road1.png", "sand": "sand1.png", "soil": "soil1.png", "water1": "water1.png", 
						  "water2": "water2.png", "water3": "water3.png"}
		self.path = "Tiles/"
		self.size = 64
		self.groundGrid = [[0] * int(WIDTH / self.size)] * int(HEIGHT / self.size)

	def createSprites(self):
		for tile in self.tiles.keys():
			self.tiles[tile] = pygame.transform.scale(pygame.image.load(self.path + self.tiles[tile]).convert(), (self.size, self.size))

	def drawGround(self, surface):
		for row in range(len(self.groundGrid)):
			for col in range(len(self.groundGrid[row])):
				surface.blit(self.tiles["grass"], (int(col * self.size), int(row * self.size), self.size, self.size))


class GameController:
	def __init__(self):
		self.running = True
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.get_surface()

		self.ground = Ground()
		self.player = Player()


	def eventLoop(self):
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				self.running = False
			if (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_w):
					self.player.direction = pygame.math.Vector2(0, -1)
				elif (event.key == pygame.K_s):
					self.player.direction = pygame.math.Vector2(0, 1)
				elif (event.key == pygame.K_a):
					self.player.direction = pygame.math.Vector2(-1, 0)
				elif (event.key == pygame.K_d):
					self.player.direction = pygame.math.Vector2(1, 0)
				self.player.isIdle = False
			if (event.type == pygame.KEYUP):
				self.player.isIdle = True



	def displayFPS(self):
		caption = f"{self.clock.get_fps():.2f}"
		pygame.display.set_caption(caption)

	def mainLoop(self):
		self.ground.createSprites()
		self.player.createSprites()

		while self.running:
			self.eventLoop()

			self.player.move()

			self.ground.drawGround(self.screen)
			self.player.drawPlayer(self.screen)

			pygame.display.update()
			self.clock.tick(GAME_FPS)			
			self.displayFPS()


if __name__ == "__main__":
	pygame.init()
	pygame.display.set_mode(SCREEN_SIZE)

	gameC = GameController()
	gameC.mainLoop()

	pygame.quit()
	sys.exit()
