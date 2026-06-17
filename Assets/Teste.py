import pygame
import random
import sys

from Const import MENU_OPTION
from Entity import Entity
from Factory import Factory

pygame.init()

fundo = pygame.image.load('./Assets/bg0.png')

# Configurações da janela
largura, altura = 600, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jan Ken Pô")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Fonte
fonte = pygame.font.SysFont(None, 40)

# Opções
opcoes = ["pedra", "papel", "tesoura"]

def desenhar_texto(texto, cor, x, y):
    img = fonte.render(texto, True, cor)
    janela.blit(img, (x, y))

def resultado(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "Você perdeu!"

def jogo_jankenpo():
    rodando = True
    mensagem = ""

    while rodando:

        janela.blit(fundo, (0,0 ))

        # Instruções na tela
        desenhar_texto("Pressione A para Pedra", PRETO, 50, 250)
        desenhar_texto("Pressione S para Papel", PRETO, 50, 300)
        desenhar_texto("Pressione D para Tesoura", PRETO, 50, 350)

        # Mensagem de resultado
        desenhar_texto(mensagem, PRETO, 50, 100)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    escolha_usuario = "pedra"
                elif evento.key == pygame.K_s:
                    escolha_usuario = "papel"
                elif evento.key == pygame.K_d:
                    escolha_usuario = "tesoura"
                else:
                    escolha_usuario = None

                if escolha_usuario:
                    escolha_computador = random.choice(opcoes)
                    mensagem = f"PC: {escolha_computador} | {resultado(escolha_usuario, escolha_computador)}"

        pygame.display.update()

