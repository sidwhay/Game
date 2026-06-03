import pygame, pygame.image, pygame.font
from pygame import Surface, Rect

from Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_WHITE


class Menu:


 def __init__(self,window):
     self.window = window
     self.surf = pygame.image.load ("./assets/teste.png").convert_alpha()
     self.rect = self.surf.get_rect()



 def run(self):
    menu_option = 0
    pygame.mixer.music.load('./Assets/bg.mp3')
    pygame.mixer.music.play(-1)
    while True:

      self.window.blit(source=self.surf, dest=self.rect)
      self.menu_text(50, "Teste", COLOR_BLACK, ((WIN_WIDTH / 2), 70))


      for i in range (len(MENU_OPTION)):
         if i == menu_option:
             self.menu_text(50, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 400 + 30 * i))
         else:
              self.menu_text(50, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 400 + 30 * i))







      for events in pygame.event.get():

        if events.type == pygame.KEYDOWN:
           if events.key == pygame.K_DOWN:
               if menu_option < len(MENU_OPTION) - 1:
                   menu_option += 1
               else:
                   menu_option = 0
        if events.type == pygame.KEYUP:
           if events.key == pygame.K_UP:
               if menu_option > 0:
                   menu_option -= 1
               else:                                     
                   menu_option = len(MENU_OPTION) - 1
           if events.key == pygame.K_RETURN:
                 return MENU_OPTION[menu_option]
                                                         






      pygame.display.flip()

 def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: pygame.Font = pygame.font.SysFont(name="arialblack", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
