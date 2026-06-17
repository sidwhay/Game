import pygame
from pygame import display

from Assets.Teste import jogo_jankenpo
from Const import COLOR_BLACK, MENU_OPTION
from Entity import Entity
from Factory import Factory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(Factory.get_entity('bg'))
        jogo_jankenpo()
        self.entity_list.append(Factory.get_entity('Player1'))

        if game_mode in [MENU_OPTION[0], MENU_OPTION[1]]:
            self.entity_list.append(Factory.get_entity('Player2'))




    def run(self):
        pygame.mixer_music.load(f'./Assets/bg.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:

         clock.tick(60)
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                 return

         self.window.fill(COLOR_BLACK)

         for ent in self.entity_list:
             self.window.blit(source=ent.surf, dest=ent.rect)
         pygame.display.flip()



            #for ent in self.entity_list:
             #   self.window.blit(source=ent.surf, rect=ent.rect)
           # pygame.display.flip()
        #pass