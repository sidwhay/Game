import pygame
import random

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)



def jankenpo_game():
    continuar = True
    while continuar:
        res = rodada()
        if res == "derrota":
            continuar = False
    return "menu"


if __name__ == "__main__":
    jankenpo_game()



largura, altura = 1000, 673
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jankenpo")



fundo = pygame.image.load("./assets/bg0.png")
fundo = pygame.transform.scale(fundo, (largura, altura))


personagem_jogador = pygame.image.load("./assets/player1.png")
personagem_jogador = pygame.transform.scale(personagem_jogador, (68, 90))

personagem_inimigo = pygame.image.load("./assets/spriteboss1.png")
personagem_inimigo = pygame.transform.scale(personagem_inimigo, (206, 189))


sprites = {
    "pedra": pygame.image.load("./Assets/pedra.png"),
    "papel": pygame.image.load("./Assets/papel.png"),
    "tesoura": pygame.image.load("./Assets/tesoura.png")
}
for chave in sprites:
    sprites[chave] = pygame.transform.scale(sprites[chave], (100, 100))


class Personagem:
    def __init__(self, nome, estilo):
        self.nome = nome
        self.estilo = estilo


    def jogar(self):
        if self.estilo == "pedra":
            escolhas = ["pedra"] * 3 + ["papel", "tesoura"]
        elif self.estilo == "papel":
            escolhas = ["papel"] * 3 + ["pedra", "tesoura"]
        elif self.estilo == "tesoura":
            escolhas = ["tesoura"] * 3 + ["pedra", "papel"]
        else:
            escolhas = list(sprites.keys())
        return random.choice(escolhas)

def resultado(jogador, inimigo):
    if jogador == inimigo:
        return "empate"


    elif (jogador == "pedra" and inimigo == "tesoura") or \
         (jogador == "papel" and inimigo == "pedra") or \
         (jogador == "tesoura" and inimigo == "papel"):
        return "vitoria"
    else:
        return "derrota"

chefe = Personagem("Janken, o Grande", "pedra")

def rodada():
    pygame.mixer.music.load("./Assets/luta.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()
    escolha_jogador = None
    escolha_inimigo = None
    resultado_final = None

    tempo_limite = 10000
    inicio = pygame.time.get_ticks()

    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))  # desenha plano de fundo


        tela.blit(personagem_jogador, (150, 533))
        tela.blit(personagem_inimigo, (700, 433))

        tempo_passado = pygame.time.get_ticks() - inicio


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN and resultado_final is None:
                if evento.key == pygame.K_a:
                    escolha_jogador = "pedra"
                elif evento.key == pygame.K_s:
                    escolha_jogador = "papel"
                elif evento.key == pygame.K_d:
                    escolha_jogador = "tesoura"


        if resultado_final is None:
            if escolha_jogador is None:
                animacao = list(sprites.keys())
                frame = (tempo_passado // 900) % 3
                tela.blit(sprites[animacao[frame]], (300, 200))  # mão jogador
            else:
                tela.blit(sprites[escolha_jogador], (300 , 200))


        if tempo_passado > tempo_limite and resultado_final is None:
            if escolha_jogador is None:
                escolha_jogador = "pedra"
            escolha_inimigo = chefe.jogar()
            resultado_final = resultado(escolha_jogador, escolha_inimigo)


        if resultado_final:
            tela.blit(sprites[escolha_jogador], (300, 200))  # mão jogador
            tela.blit(sprites[escolha_inimigo], (600, 200))  # mão inimigo
            pygame.display.update()
            pygame.time.delay(1500)
            return resultado_final

        pygame.display.update()

def batalha():
    continuar = True
    while continuar:

        res = rodada()
        jankenpo_game()
        if res == "derrota":
            pygame.quit()




