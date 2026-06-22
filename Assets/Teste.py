import pygame
import math

pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Texto Flutuante")

def tela_texto_flutuante(mensagem: str, callback=None):
    """
    Exibe uma tela com texto flutuante.
    Se o jogador apertar Enter, chama a função 'callback'.
    """
    fonte = pygame.font.SysFont("arialblack", 60)
    texto = fonte.render(mensagem, True, (255, 255, 255))

    x = largura // 2
    y_base = altura // 2
    angulo = 0

    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if callback:   # se foi passada uma função
                        callback()
                    rodando = False

        tela.fill((0, 0, 0))  # fundo preto

        # Movimento flutuante (seno para cima/baixo)
        y = y_base + math.sin(angulo) * 20
        angulo += 0.05

        rect = texto.get_rect(center=(x, y))
        tela.blit(texto, rect)

        pygame.display.update()
        clock.tick(60)

# Exemplo de função que será chamada
def iniciar_batalha():
    print("Chamando a função de batalha...")

# Uso da tela
if __name__ == "__main__":
    tela_texto_flutuante("Pressione ENTER para começar!", iniciar_batalha)
