import pygame



from Const import COLOR_BLACK, MENU_OPTION
from Entity import Entity
from Factory import Factory
from jankenpo import jankenpo_game

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        jankenpo_game()




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
             elif event.key == pygame.K_DOWN:
                 resultado = jankenpo_game()
                 if resultado == "menu":
                     pass


         self.window.fill(COLOR_BLACK)

         for ent in self.entity_list:
             self.window.blit(source=ent.surf, dest=ent.rect)
         pygame.display.flip()



            #for ent in self.entity_list:
             #   self.window.blit(source=ent.surf, rect=ent.rect)
           # pygame.display.flip()
        #pass