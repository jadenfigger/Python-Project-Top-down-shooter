import sys
import os
import levels
import pygame

WIDTH, HEIGHT = SCREEN_SIZE = (1024, 640)
GAME_FPS = 60
frameCount = 0

os.chdir('..')


class Player:
    def __init__(self):
        self.direction = pygame.math.Vector2(0, 1)
        self.playerWidHei = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)

        self.rollSpeed = 4
        self.moveSpeed = 2

        self.isIdle = True
        self.isRolling = False

        self.walkingSprites = {"up": [], "up-right": [], "right": [], "down-right": [],
                               "down": [], "down-left": [], "left": [], "up-left": []}
        self.walkingSpritePaths = ["Character_Up.png", "Character_UpRight.png", "Character_Right.png",
                                   "Character_DownRight.png",
                                   "Character_Down.png", "Character_DownLeft.png", "Character_Left.png",
                                   "Character_UpLeft.png"]
        self.rollingSprites = {"up": [], "up-right": [], "right": [], "down-right": [],
                               "down": [], "down-left": [], "left": [], "up-left": []}
        self.rollingSpritePaths = ["Character_RollUp.png", "Character_RollUpRight.png", "Character_RollRight.png",
                                   "Character_RollDownRight.png",
                                   "Character_RollDown.png", "Character_RollDownLeft.png", "Character_RollLeft.png",
                                   "Character_RollUpLeft.png"]
        self.currentSprite = None
        self.facing = None
        self.animationFrame = 0
        self.animationDelayCount = 0
        self.framesBetweenRolls = 60
        self.startOfRoll = -self.framesBetweenRolls

    def createSprites(self):
        for i in range(len(self.walkingSpritePaths)):
            self.walkingSpritePaths[i] = pygame.image.load("Characters/" + self.walkingSpritePaths[i])
            self.rollingSpritePaths[i] = pygame.image.load("Characters/" + self.rollingSpritePaths[i])

        count = 0
        for direction in self.walkingSprites:
            for i in range(4):
                self.walkingSprites[direction].append(pygame.transform.scale(self.walkingSpritePaths[count].subsurface(
                    (8 + i * 32, 6, 16, 22)), (48, 66)))
                self.rollingSprites[direction].append(pygame.transform.scale(self.rollingSpritePaths[count].subsurface(
                    (8 + i * 32, 6, 17, 22)), (48, 66)))  # 17 add last pixel for some rolling sprites
            count += 1

        self.facing = "up"
        self.currentSprite = self.walkingSprites[self.facing]
        self.playerWidHei = pygame.math.Vector2(self.currentSprite[self.animationFrame].get_size())

    def drawPlayer(self, surface):
        if self.direction.x < 0 and self.direction.y < 0:
            self.facing = "up-left"
        elif self.direction.x < 0 and self.direction.y > 0:
            self.facing = "down-left"
        elif self.direction.x > 0 and self.direction.y < 0:
            self.facing = "up-right"
        elif self.direction.x > 0 and self.direction.y > 0:
            self.facing = "down-right"
        elif self.direction.x < 0 and self.direction.y == 0:
            self.facing = "left"
        elif self.direction.x > 0 and self.direction.y == 0:
            self.facing = "right"
        elif self.direction.x == 0 and self.direction.y < 0:
            self.facing = "up"
        elif self.direction.x == 0 and self.direction.y > 0:
            self.facing = "down"

        self.drawAnimation()
        surface.blit(self.currentSprite, (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))

    def drawAnimation(self):
        if not self.isRolling:
            if self.isIdle:
                self.animationFrame = 0
                self.currentSprite = self.walkingSprites[self.facing][self.animationFrame]
            else:
                if self.animationDelayCount % 10 == 0:
                    self.animationFrame += 1

                if self.animationFrame >= len(self.walkingSprites[self.facing]):
                    self.animationFrame = 0

                self.currentSprite = self.walkingSprites[self.facing][self.animationFrame]
                self.animationDelayCount += 1
        else:
            if self.startOfRoll == frameCount:
                self.animationFrame = 0

            if self.animationFrame >= len(self.walkingSprites[self.facing]):
                self.isRolling = False
                self.animationFrame = 0

            self.currentSprite = self.rollingSprites[self.facing][self.animationFrame]
            self.animationDelayCount += 1

            if self.animationDelayCount % 5 == 0:
                self.animationFrame += 1

    def move(self):
        keys = pygame.key.get_pressed()
        initialPosition = pygame.math.Vector2(self.pos.x, self.pos.y)
        move = pygame.math.Vector2(0, 0)

        x = 0
        y = 0

        if keys[119]:
            y = -1
        elif keys[115]:
            y = 1
        if keys[97]:
            x = -1
        elif keys[100]:
            x = 1

        if move.x != 0 and move.y != 0:
            x *= 0.707106
            y *= 0.706106

        if (keys[32] and (
                x != 0 or y != 0) and not self.isRolling and frameCount > self.startOfRoll + self.framesBetweenRolls):
            self.isRolling = True
            self.animationDelayCount = 0
            self.startOfRoll = frameCount

        if self.isRolling:
            move = pygame.math.Vector2(x * self.rollSpeed, y * self.rollSpeed)
        else:
            move = pygame.math.Vector2(x * self.moveSpeed, y * self.moveSpeed)

        self.pos += move
        if self.pos.y != initialPosition.y:
            self.direction.y = self.pos.y - initialPosition.y
        else:
            self.direction.y = 0

        if self.pos.x != initialPosition.x:
            self.direction.x = self.pos.x - initialPosition.x
        else:
            self.direction.x = 0

        if self.pos == initialPosition:
            self.isIdle = True
        else:
            if not self.isRolling:
                self.animationDelayCount = 0
            self.isIdle = False


class Ground:
    def __init__(self):
        self.tiles = {'dirt': 'Dirt Texture.jpg', 'grass': 'Grass Texture.jpg', 'road': 'Road Texture.jpg',
                      'sand': 'Sand Texture.jpg', 'soil': 'Soil Texture.jpg', 'stone': 'Stone Texture.jpg',
                      'water': 'Water Texture.png'}
        self.path = "Textures/"
        self.size = 32
        self.groundGrid = None

    def createSprites(self):
        for tile in self.tiles.keys():
            self.tiles[tile] = pygame.transform.scale(pygame.image.load(self.path + self.tiles[tile]).convert(),
                                                      (self.size, self.size))

    def drawGround(self, surface):
        for row in range(len(self.groundGrid)):
            for col in range(len(self.groundGrid[row])):
                surface.blit(self.tiles[self.groundGrid[row][col]], (
                    int(col * self.size), int(row * self.size), self.size, self.size))

    def set_groundGrid(self, level):
        self.groundGrid = levels.getLevel(level)


class GameController:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.ground = Ground()
        self.player = Player()
        self.Level = 0

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def displayFPS(self):
        caption = f"{self.clock.get_fps():.2f}"
        pygame.display.set_caption(caption)

    def checkLevel(self):
        if self.player.pos.y >= HEIGHT:
            self.Level += 1
            self.ground.set_groundGrid(self.Level)
            self.player.pos = pygame.math.Vector2(self.player.pos.x, -self.player.playerWidHei.y / 2)
        elif self.player.pos.y < -self.player.playerWidHei.y:
            self.Level -= 1
            self.ground.set_groundGrid(self.Level)
            self.player.pos = pygame.math.Vector2(self.player.pos.x, HEIGHT - self.player.playerWidHei.y / 2)
        print(self.Level)

    def mainLoop(self):
        global frameCount

        self.ground.createSprites()
        self.player.createSprites()

        self.ground.set_groundGrid(self.Level)

        while self.running:
            self.eventLoop()

            self.player.move()
            self.checkLevel()

            self.ground.drawGround(self.screen)
            self.player.drawPlayer(self.screen)

            pygame.display.update()
            self.clock.tick(GAME_FPS)
            self.displayFPS()
            frameCount += 1


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)

    gameC = GameController()
    gameC.mainLoop()

    pygame.quit()
    sys.exit()
