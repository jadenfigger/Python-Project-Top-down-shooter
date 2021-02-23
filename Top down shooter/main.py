import pygame
import sys

WIDTH, HEIGHT = SCREEN_SIZE = (1024, 768)
GAME_FPS = 60

class Player:
	def __init__(self):
		self.direction = pygame.math.Vector2(0, 1)
		self.playerWidHei = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
		self.moveSpeed = 3
		self.rotationAngle = 0
		self.rotationSpeed = 1

		self.isIdle = True

		self.sprites = {"idle": [None] * 4, "up": [None] * 8, "down": [None] * 8, "right": [None] * 8, "left": [None] * 8}
		self.walkingSpriteSheet = pygame.image.load("Characters/BODY_male_walking.png")
		self.currentSprite = None

	def createSprites(self):
		# x: 16 y: 14, x: 49 y: 63  xWidth = 33 yHeight = 49  yBuffer = 15
		for i in range(4):
			self.sprites["idle"][i] = self.walkingSpriteSheet.subsurface((16, 14 + (i * 64), 33, 49))
		self.playerWidHei = pygame.math.Vector2(self.sprites["idle"][i].get_size())
		self.currentSprite = self.sprites["idle"][2]


	def drawPlayer(self, surface):
		print(self.direction)
		'''if (self.direction == (0, -self.moveSpeed)):
			self.currentSprite = self.sprites["idle"][0]
		elif (self.direction == (-self.moveSpeed, 0)):
			self.currentSprite = self.sprites["idle"][1]
		elif (self.direction == (0, self.moveSpeed)):
			self.currentSprite = self.sprites["idle"][2]
		elif (self.direction == (self.moveSpeed, 0)):
			self.currentSprite = self.sprites["idle"][3]'''
		
		if self.direction.x < 0:
			self.currentSprite = self.sprites['idle'][1]
		elif self.direction.x > 0:
			self.currentSprite = self.sprites['idle'][3]
		elif self.direction.y < 0:
			self.currentSprite = self.sprites['idle'][0]
		elif self.direction.y > 0:
			self.currentSprite = self.sprites['idle'][2]

		surface.blit(self.currentSprite, (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))

	def move(self): 
		# w = 119
		# a = 97
		# s = 115
		# d = 100
		# space = 32
		keys = pygame.key.get_pressed()
		initialPosition = pygame.math.Vector2(self.pos.x, self.pos.y)

		if (keys[119]):
			self.pos.y += -1 * self.moveSpeed
		elif (keys[115]):
			self.pos.y += 1 * self.moveSpeed
		if (keys[97]):
			self.pos.x += -1 * self.moveSpeed
		elif (keys[100]):
			self.pos.x += 1 * self.moveSpeed


		if (self.pos.y != initialPosition.y):
			self.direction.y = self.pos.y - initialPosition.y
		else: 
			self.direction.y = 0

		if (self.pos.x != initialPosition.x):
			self.direction.x = self.pos.x - initialPosition.x
		else:
			self.direction.x = 0


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
