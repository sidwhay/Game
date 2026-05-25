import pygame
from const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        self.window = None



    def run(self, ):
      print('setup start')
      pygame.init()
      window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))
      print('setup end')


      print('Loop Start')
      while True:
       for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()


