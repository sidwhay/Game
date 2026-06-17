import pygame
import random

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# ... todas as funções e classes que você já tem ...

def jankenpo_game():
    continuar = True
    while continuar:
        res = rodada()
        if res == "derrota":
            continuar = False
    return "menu"

# só roda automaticamente se você executar este arquivo diretamente
if __name__ == "__main__":
    jankenpo_game()


# Tela
largura, altura = 1000, 673
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jankenpo estilo Alex Kidd")

# Música
pygame.mixer.music.load("./Assets/bg.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

# Plano de fundo
fundo = pygame.image.load("./assets/bg0.png")
fundo = pygame.transform.scale(fundo, (largura, altura))

# Personagens
personagem_jogador = pygame.image.load("./assets/player1.png")
personagem_jogador = pygame.transform.scale(personagem_jogador, (68, 90))

personagem_inimigo = pygame.image.load("./assets/spriteboss1.png")
personagem_inimigo = pygame.transform.scale(personagem_inimigo, (206, 189))

# Sprites das mãos
sprites = {
    "pedra": pygame.image.load("./assets/teste.png"),
    "papel": pygame.image.load("./assets/spriteboss1.png"),
    "tesoura": pygame.image.load("./assets/player1.png")
}
for chave in sprites:
    sprites[chave] = pygame.transform.scale(sprites[chave], (100, 100))

# Inimigo
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
    escolha_jogador = None
    escolha_inimigo = None
    resultado_final = None

    tempo_limite = 3000
    inicio = pygame.time.get_ticks()

    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))  # desenha plano de fundo

        # desenha personagens
        tela.blit(personagem_jogador, (150, 533))
        tela.blit(personagem_inimigo, (700, 433))

        tempo_passado = pygame.time.get_ticks() - inicio

        # Captura escolha
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

        # Suspense
        if resultado_final is None:
            if escolha_jogador is None:
                animacao = list(sprites.keys())
                frame = (tempo_passado // 300) % 3
                tela.blit(sprites[animacao[frame]], (300, 200))  # mão jogador
            else:
                tela.blit(sprites[escolha_jogador], (150, 200))

        # Revela jogadas
        if tempo_passado > tempo_limite and resultado_final is None:
            if escolha_jogador is None:
                escolha_jogador = "pedra"
            escolha_inimigo = chefe.jogar()
            resultado_final = resultado(escolha_jogador, escolha_inimigo)

        # Mostrar resultado final
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
        if res == "derrota":
            continuar = False


