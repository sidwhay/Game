from subprocess import STARTUPINFO

import pygame
print('setup start')
pygame.init()
window = pygame.display.set_mode(size = (800, 600))
print('setup end')


print('Loop Start')
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
