import pygame, pygame.image, pygame.font
from pygame import Surface, Rect

from Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION


class Menu:

 def __init__(self,window):
     self.window = window
     self.surf = pygame.image.load ("./assets/teste.png")
     self.rect = self.surf.get_rect()



 def run(self):
    pygame.mixer.music.load('./assets/bg.mp3')
    pygame.mixer.music.play(-1)
    while True:

     self.window.blit(source=self.surf, dest=self.rect)
     self.menu_text(50, "Teste", COLOR_BLACK, ((WIN_WIDTH / 2), 70))


     for i in range (len(MENU_OPTION)):
         self.menu_text(50, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 400 + 30 * i))

     pygame.display.flip()




     for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()


 def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: pygame.Font = pygame.font.SysFont(name="arialblack", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
