import sys
import os
import levels
import enemies
import pygame
import random
from math import floor, atan2, pi, degrees

WIDTH, HEIGHT = SCREEN_SIZE = (1024, 640)
GAME_FPS = 60
LEVEL = 0
frameCount = 0

# os.chdir('..')

# print(os.getcwd())

class Player:
    def __init__(self):
        self.direction = pygame.math.Vector2(0, 1)
        self.playerWidHei = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)

        self.rollSpeed = 4
        self.moveSpeed = 2

        self.maxHealth = 40 
        self.currentHealth = self.maxHealth
        self.attackDamage = 5
        self.attackingDistance = 70

        self.attackRange = {"up-right": [270, 90], "down-right": [270, 90],
                            "down-left": [90, 270], "up-left": [90, 270]}

        self.dealDamage = False
        self.isIdle = True
        self.isRolling = False
        self.isAttacking = False

        self.swordTranslations = {"up-right": [-24-48, 7-69], "down-right": [-36-48, 5-69],
                                  "down-left": [-24-48, 3-69], "up-left": [-15-48, 6-69]}

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
        self.attackingSprites = {"up-right": [], "down-right": [], "down-left": [], "up-left": []}
        self.attackingSpritePaths = ["Character_SlashUpRight.png", "Character_SlashDownRight.png",
                                     "Character_SlashDownLeft.png", "Character_SlashUpLeft.png"]
        self.swordSprites = {"up-right": [], "down-right": [], "down-left": [], "up-left": []}
        self.swordSpritePaths = ["Sword_UpRight.png", "Sword_DownRight.png", "Sword_DownLeft.png", "Sword_UpLeft.png"]

        self.currentSprite = None
        self.swordSprite = None
        self.facing = "up"
        self.facingAttack = "up-right"
        self.animationFrame = 0
        self.animationDelayCount = 0
        self.framesBetweenRolls = 60
        self.framesBetweenAttacks = 10
        self.startOfAttack = -self.framesBetweenAttacks
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
                    (8 + i * 32, 6, 17, 22)), (51, 66)))
            count += 1

        for i in range(len(self.attackingSpritePaths)):
            self.attackingSpritePaths[i] = pygame.image.load("Characters/" + self.attackingSpritePaths[i])
            self.swordSpritePaths[i] = pygame.image.load("Characters/" + self.swordSpritePaths[i])

        count = 0
        for direction in self.attackingSprites:
            for i in range(5):
                self.attackingSprites[direction].append(pygame.transform.scale(
                    self.attackingSpritePaths[count].subsurface((8 + i * 32, 5, 17, 23)), (51, 69)))
                self.swordSprites[direction].append(pygame.transform.scale(
                    self.swordSpritePaths[count].subsurface((i * 64, 0, 64, 64)), (192, 192)))
            count += 1

        self.facing = "up"
        self.currentSprite = self.walkingSprites[self.facing]
        self.playerWidHei = pygame.math.Vector2(self.currentSprite[self.animationFrame].get_size())

    def drawPlayer(self, surface):
        if self.isRolling:
            if self.startOfRoll == frameCount:
                self.animationFrame = 0

            if self.animationFrame >= len(self.walkingSprites[self.facing]):
                self.isRolling = False
                self.animationFrame = 0

            self.currentSprite = self.rollingSprites[self.facing][self.animationFrame]
            self.animationDelayCount += 1

            if self.animationDelayCount % 5 == 0:
                self.animationFrame += 1
        elif self.isAttacking and not self.isRolling:
            if self.startOfAttack == frameCount:
                self.animationFrame = 0

            if self.animationDelayCount % 6 == 0 and self.startOfAttack != frameCount:
                self.animationFrame += 1

            if self.animationFrame >= len(self.attackingSprites[self.facingAttack]):
                self.isAttacking = False
                self.animationFrame = 0
                return

            if (self.animationFrame == 3):
                self.dealDamage = True
            else:
                self.dealDamage = False

            self.currentSprite = self.attackingSprites[self.facingAttack][self.animationFrame]
            self.swordSprite = self.swordSprites[self.facingAttack][self.animationFrame]
            self.animationDelayCount += 1
        elif (not self.isIdle) and (not self.isAttacking) and (not self.isRolling):
            if self.animationDelayCount % 5 == 0:
                self.animationFrame += 1

            if self.animationFrame >= len(self.walkingSprites[self.facing]):
                self.animationFrame = 0

            self.currentSprite = self.walkingSprites[self.facing][self.animationFrame]
            self.animationDelayCount += 1
        else:
            self.animationFrame = 0
            self.currentSprite = self.walkingSprites[self.facing][self.animationFrame]

        surface.blit(self.currentSprite, (self.pos.x, self.pos.y, self.playerWidHei.x, self.playerWidHei.y))
        if self.isAttacking and not self.isRolling and self.swordSprite is not None:
            surface.blit(self.swordSprite, (int(self.pos.x + self.swordTranslations[self.facingAttack][0]),
                                            int(self.pos.y + self.swordTranslations[self.facingAttack][1]),
                                            self.playerWidHei.x, self.playerWidHei.y))

        sHeathBarBack = pygame.Surface((int(self.playerWidHei.x), 8))
        sHeathBarBack.set_alpha(100)
        sHeathBarBack.fill((0, 0, 0))
        surface.blit(sHeathBarBack, (self.pos.x, self.pos.y - 8))
        pygame.draw.rect(surface, (255, 0, 0), (self.pos.x, self.pos.y-8, int((48 * self.currentHealth/self.maxHealth)), 8))

    def playerInput(self, keys):
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

        if (keys[32] and (x != 0 or y != 0) and not self.isRolling and
                frameCount > self.startOfRoll + self.framesBetweenRolls and not self.isAttacking):
            self.isRolling = True
            self.animationDelayCount = 0
            self.startOfRoll = frameCount

        if keys[106] and not self.isRolling:
            self.isAttacking = True
            self.animationDelayCount = 0
            self.startOfAttack = frameCount

        self.move(x, y)

        self.determineFacing()

    def move(self, x, y):
        initialPosition = pygame.math.Vector2(self.pos.x, self.pos.y)

        if self.isAttacking:
            x = 0
            y = 0
 
            x *= 0.707106
            y *= 0.706106

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
            self.isIdle = False

    def determineFacing(self):
        if self.direction.x < 0 and self.direction.y < 0:
            self.facing = "up-left"
            self.facingAttack = "up-left"
        elif self.direction.x < 0 and self.direction.y > 0:
            self.facing = "down-left"
            self.facingAttack = "down-left"
        elif self.direction.x > 0 and self.direction.y < 0:
            self.facing = "up-right"
            self.facingAttack = "up-right"
        elif self.direction.x > 0 and self.direction.y > 0:
            self.facing = "down-right"
            self.facingAttack = "down-right"
        elif self.direction.x < 0 and self.direction.y == 0:
            self.facing = "left"
            self.facingAttack = "down-left"
        elif self.direction.x > 0 and self.direction.y == 0:
            self.facing = "right"
            self.facingAttack = "up-right"
        elif self.direction.x == 0 and self.direction.y < 0:
            self.facing = "up"
            self.facingAttack = "up-left"
        elif self.direction.x == 0 and self.direction.y > 0:
            self.facing = "down"
            self.facingAttack = "down-right"

class Ground:
    def __init__(self):
        self.tiles = {'dirt': 'Dirt Texture.jpg', 'grass': 'Grass Texture.png', 'road': 'Road Texture.png',
                      'sand': 'Sand Texture.jpg', 'soil': 'Soil Texture.jpg', 'stone': 'Stone Texture.jpg',
                      'water': 'Water Texture.png'}
        self.path = "Textures/"
        self.size = 32
        self.groundGrid = levels.getLevel(LEVEL)

    def createSprites(self):
        for tile in self.tiles.keys():
            self.tiles[tile] = pygame.transform.scale(pygame.image.load(self.path + self.tiles[tile]).convert(),
                                                      (self.size, self.size))

    def drawGround(self, surface):
        for row in range(len(self.groundGrid)):
            for col in range(len(self.groundGrid[row])):
                surface.blit(self.tiles[self.groundGrid[row][col]], (
                    int(col * self.size), int(row * self.size), self.size, self.size))

    def createMatrix(self):
        matrix = []
        for i in range(len(self.groundGrid)):
            matrix.append([])
            for j in range(len(self.groundGrid[i])):
                matrix[i].append(1)

        return matrix

    def set_groundGrid(self, level):
        if (level >= 0) and (level < levels.getSize()):
            self.groundGrid = levels.getLevel(level)
            return True
        else:
            return False

class GameController:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.keys = None

        self.skeletonMeleeEnemies = []

        self.ground = Ground()
        self.player = Player()
        self.enemy = enemies.Enemy()

        self.matrix = self.ground.createMatrix()

        self.enemySpawnPositions = [(16, 16), (16, 176), (16, 304), (16, 496), (16, 624), (176, 16), (304, 16), (496, 16), (624, 16),
                                    (176, 624), (304, 624), (496, 624), (624, 624)]

        self.Level = 0

        self.levelsSpawnDetails = [3, 4, 5]
        self.spawnedEnemies = 0
        self.spawnEnemyOnFrame = None


    def eventLoop(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
 
    def displayFPS(self):
        caption = f"{self.clock.get_fps():.2f}"
        pygame.display.set_caption(caption)

    
    def spawnEnemy(self):
        self.skeletonMeleeEnemies.append(enemies.MeleeSkeletonEnemy(
        pygame.math.Vector2(self.enemySpawnPositions[random.randint(0, len(self.enemySpawnPositions)) - 1])))
        self.spawnedEnemies += 1



    def checkLevel(self):
        if (self.player.pos.y > HEIGHT - self.player.playerWidHei[1] and len(self.skeletonMeleeEnemies) != 0):
            self.player.pos.y -= self.player.moveSpeed
            return

        if self.player.pos.y >= HEIGHT:
            self.Level += 1
            self.spawnedEnemies = 0
            self.spawnEnemyOnFrame = frameCount + 60
            if self.ground.set_groundGrid(self.Level):
                self.player.pos = pygame.math.Vector2(self.player.pos.x, -self.player.playerWidHei.y / 2)
            else:
                self.Level -= 1
        elif self.player.pos.y < -self.player.playerWidHei.y:
            self.Level -= 1
            if self.ground.set_groundGrid(self.Level):
                self.player.pos = pygame.math.Vector2(self.player.pos.x, HEIGHT - self.player.playerWidHei.y / 2)
            else:
                self.Level += 1
                self.spawnedEnemies = 0



    def mainLoop(self):
        global frameCount

        self.ground.createSprites()
        self.player.createSprites()

        self.spawnEnemy()

        while self.running:
            self.eventLoop()

            self.player.playerInput(self.keys)
            self.checkLevel()

            if (self.spawnEnemyOnFrame != 0):
                if (frameCount == self.spawnEnemyOnFrame):
                    self.spawnEnemy()

            self.ground.drawGround(self.screen)
            
            toBeDeleted = []
            for i in range(len(self.skeletonMeleeEnemies)):
                if (self.skeletonMeleeEnemies[i].currentHealth <= 0):
                   toBeDeleted.append(i)

                self.skeletonMeleeEnemies[i].moveToTarget(self.player.pos, self.matrix, self.ground.size)
                self.skeletonMeleeEnemies[i].drawEnemy(self.screen, self.player.pos)

                if (self.skeletonMeleeEnemies[i].dealDamage):
                    self.player.currentHealth -= self.skeletonMeleeEnemies[i].attackDamage

            for i in toBeDeleted:
                del self.skeletonMeleeEnemies[i]
                if (self.spawnedEnemies < self.levelsSpawnDetails[self.Level]):
                    self.spawnEnemy()
                

            toBeDeleted = []
            if (frameCount % 210 == 0 and self.player.currentHealth != self.player.maxHealth):
                self.player.currentHealth += 3
            if (self.player.currentHealth <= 0):
                self.running = False

            self.player.drawPlayer(self.screen)

            if (self.player.dealDamage):
                for i in range(len(self.skeletonMeleeEnemies)):
                   if (self.player.pos.distance_to(self.skeletonMeleeEnemies[i].pos) < self.player.attackingDistance):
                        dx = float(self.skeletonMeleeEnemies[i].pos.x - self.player.pos.x)
                        dy = float(self.skeletonMeleeEnemies[i].pos.y - self.player.pos.y)
                        rads = atan2(-dy, dx)
                        rads %= 2*pi
                        deg = degrees(rads)
                        if (self.player.attackRange[self.player.facingAttack][0] <= deg <= self.player.attackRange[self.player.facingAttack][1] or 
                            (deg >= self.player.attackRange[self.player.facingAttack][1] or deg <= self.player.attackRange[self.player.facingAttack][0])):
                            self.skeletonMeleeEnemies[i].currentHealth -= self.player.attackDamage

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
