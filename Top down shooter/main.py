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

		self.sprites = {"up": [None] * 4, "up-right": [None] * 4, "right": [None] * 4, "right-down": [None] * 4, 
					    "down": [None] * 4, "down-left": [None] * 4, "left": [None] * 4, "top-left": [None] * 4}
		self.spritePaths = ["Character_Up.png", "Character_UpRight.png", "Character_Right.png", "Character_DownRight.png"
							"Character_Down.png", "Character_DownLeft.png", "Character_Left.png", "Character_UpLeft.png"]
		self.currentSprite = None

	def createSprites(self):
		for i in range(len(self.spritePaths)):
			self.spritePaths[i] = pygame.image.load("Characters/" + self.spritePaths[i])

		print(self.spritePaths)
		# for key in self.sprites:
		# 	self.sprites[key][i] = self.walkingSpriteSheet.subsurface((16, 14 + (i * 64), 33, 49))
		# self.playerWidHei = pygame.math.Vector2(self.sprites["idle"][i].get_size())
		# self.currentSprite = self.sprites["idle"][2]


	def drawPlayer(self, surface):
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

			# self.player.move()

			self.ground.drawGround(self.screen)
			# self.player.drawPlayer(self.screen)

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
