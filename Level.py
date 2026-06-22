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

        if self.game_mode == MENU_OPTION[0]:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("./Assets/luta.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            jankenpo_game()

        elif self.game_mode == MENU_OPTION[1]:
            imagem = pygame.image.load("./Assets/controles.png").convert_alpha()
            largura = self.window.get_width()
            altura = self.window.get_height()
            imagem = pygame.transform.scale(imagem, (largura, altura))
            rect = imagem.get_rect(center=(largura // 2, altura // 2))
            rodando = True
            while rodando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("./Assets/luta.mp3")
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.set_volume(0.3)
                            jankenpo_game()
                self.window.fill(COLOR_BLACK)
                self.window.blit(imagem, rect)
                pygame.display.flip()

    def run(self):
        pygame.mixer_music.load('./Assets/menu.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:

         clock.tick(60)
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
             elif event.type == pygame.K_DOWN:
                if event.key == pygame.K_DOWN:
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