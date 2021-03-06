import pygame

class RayCaster(object):
    def __init__(self, screen):
        sef.screen = screen

        _,_, self.width, self.height = screen.get_rect()

        self.map = []
        self.blocksize = 50
        self.wallheight = 50

    def load_map(self, filename):
        with open(filename) as file:
            for line in file.readline():
                self.map


pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL )
screen.set_alpha(None)

rCaster = RayCaster(screen)
rCaster.load_map("map.txt")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps

isRunning = True
while isRunning:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT():
            isRunning = False

    screen.fill(pygame.Color("gray"))

    #fps
    screen.fill(pygame.Color("black"), (0, 0, 30, 30) )
    screen.blit(updateFPS(), (0,0))

    clock.tick(90)

    pygame.display.update()

pygame.quit()