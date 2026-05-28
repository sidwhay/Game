import pygame

from Entity import Entity
from Factory import Factory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Factory.get_entity('bg'))







    def run (self):
      while True:
          for ent in self.entity_list:
              self.window.blit(source=ent.surf, rect=ent.rect)
          pygame.display.flip()

    pass