import sys
import pygame
import levels

WIDTH, HEIGHT = SCREEN_SIZE = (1024, 640)
GAME_FPS = 60
LEVEL = 0


# TODO Merge ground.py with newest main.py
# TODO change level when level over and player goes off bottom of screen
class Ground:
    def __init__(self):
        self.tiles = {'dirt': 'Dirt Texture.jpg', 'grass': 'Grass Texture.jpg', 'road': 'Road Texture.jpg',
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
                    int(col * self.size), int(row * self.size), self.size, self.size))  # change to the random array


class GameController:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.ground = Ground()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def displayFPS(self):
        caption = f"{self.clock.get_fps():.2f}"
        pygame.display.set_caption(caption)

    def mainLoop(self):
        self.ground.createSprites()

        while self.running:
            self.eventLoop()

            self.ground.drawGround(self.screen)

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
