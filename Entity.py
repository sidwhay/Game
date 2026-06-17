from abc import ABC

import pygame.image



class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Assets/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @staticmethod
    def move(self, ):
        pass

