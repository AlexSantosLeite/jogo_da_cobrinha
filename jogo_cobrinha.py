import pygame
import random
import time

# Configurações iniciais
largura = 720
altura = 480
tamanho_bloco = 10
velocidade = 15

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Inicialização do pygame
pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")
fps = pygame.time.Clock()

# Funções auxiliares
def mostrar_cobra(lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, azul, pygame.Rect(bloco[0], bloco[1], tamanho_bloco, tamanho_bloco))

def mostrar_comida(pos):
    pygame.draw.rect(tela, vermelho, pygame.Rect(pos[0], pos[1], tamanho_bloco, tamanho_bloco))

def mostrar_texto(texto, cor, pos):
    fonte = pygame.font.Font(None, 36)
    texto_surface = fonte.render(texto, True, cor)
    tela.blit(texto_surface, pos)

# Função do jogo
def jogo():
    # Posição inicial da cobra
    pos_x = largura // 2
    pos_y = altura // 2

    # Lista para representar a cobra
    cobra = [[pos_x, pos_y]]

    # Direção inicial
    direcao = 'direita'

    # Posição da comida
    comida = [
        random.randrange(1, (largura // tamanho_bloco)) * tamanho_bloco,
        random.randrange(1, (altura // tamanho_bloco)) * tamanho_bloco
    ]

    jogando = True
    while jogando:
        # Processamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != 'baixo':
                    direcao = 'cima'
                elif evento.key == pygame.K_DOWN and direcao != 'cima':
                    direcao = 'baixo'
                elif evento.key == pygame.K_LEFT and direcao != 'direita':
                    direcao = 'esquerda'
                elif evento.key == pygame.K_RIGHT and direcao != 'esquerda':
                    direcao = 'direita'

        # Atualizar a posição da cobra
        if direcao == 'cima':
            pos_y -= tamanho_bloco
        elif direcao == 'baixo':
            pos_y += tamanho_bloco
        elif direcao == 'esquerda':
            pos_x -= tamanho_bloco
        elif direcao == 'direita':
            pos_x += tamanho_bloco

        cobra.insert(0, [pos_x, pos_y])

        # Verificar se a cobra comeu a comida
        if pos_x == comida[0] and pos_y == comida[1]:
            comida = [
                random.randrange(1, (largura // tamanho_bloco)) * tamanho_bloco,
                random.randrange(1, (altura // tamanho_bloco)) * tamanho_bloco
            ]
        else:
            cobra.pop()

        # Verificar colisões
        if (
            pos_x >= largura or
            pos_x < 0 or
            pos_y >= altura or
            pos_y < 0 or
            [pos_x, pos_y] in cobra[1:]
        ):
            mostrar_texto("Game Over", vermelho, [largura // 3, altura // 3])
            pygame.display.flip()
            time.sleep(2)  # Espera para mostrar a mensagem de "Game Over"
            jogando = False  # Sai do loop para encerrar o jogo

        # Limpar e desenhar a tela
        tela.fill(preto)
        mostrar_cobra(cobra)
        mostrar_comida(comida)

        pygame.display.flip()
        fps.tick(velocidade)

    # Reiniciar o jogo manualmente após a saída do loop
    jogo()  # Reinicia o jogo ao sair do loop

# Iniciar o jogo
jogo()

pygame.quit()  # Encerra o pygame quando o jogo termina
