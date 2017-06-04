########################################################################
#
# Jogadores
#
#   O nome dos jogadores serão representados por uma lista de duas
# posições onde cada posição contém uma string com o nome do jogador.
# Note que a CPU também é considerada um jogador.
#
#   Exemplo:
#       jogadores = ["Jusama", "Jeffinho"]
#
########################################################################

########################################################################
#
# Símbolos
#
#   Os caracteres usados pra marcar o tabuleiro serão representados por
# uma lista de duas posições onde cada posição contém um caractere com
# um símbolo. Por default, os símbolos são "X" e "O".
#
#   Exemplo:
#       simbolos = ["+", "."]
#
########################################################################

########################################################################
#
# Tabuleiro
#
#   O tabuleiro do jogo da velha será representado como uma lista de
# tamanho 10, ao invés de uma matriz 3 por 3. O índice 0 da lista
# deve ser ignorado.
#
#   Significado de cada elemento possível no tabuleiro:
#       > O inteiro zero significa que aquela posição ainda não foi
#           marcada por nenhum jogador;
#       > simbolos[0] significa que aquela posição foi marcada pelo
#           jogadores[0];
#       > simbolos[1] significa que aquela posição foi marcada pelo
#           jogadores[1].
#
#   Visualização da representação dos índices do tabuleiro:
#       1 2 3
#       4 5 6
#       7 8 9
#
########################################################################

CPU_FACIL = "CPU (fácil)" # constante global
CPU_DIFICIL = "CPU (difícil)" # constante global

def mostraTelaJogo(tabuleiro, jogadores, simbolos):
    """Não possui retorno. Imprime a interface do jogo com o tabuleiro
    e nome dos jogadores"""
    # Aqui há mais liberdade, já que é a parte gráfica.

def podeJogar(tabuleiro):
    """Retorna verdadeiro se ainda é possível fazer alguma jogada,
    caso contrário, falso"""

def cpuFacilJogada(tabuleiro):
    """Retorna um inteiro que representa a posição de uma jogada
    válida da CPU fácil (escolha aleatória)"""

def cpuDificilJogada(tabuleiro):
    """Retorna um inteiro que representa a posição de uma jogada
    válida da CPU difícil (jogada ótima, a CPU difícil não perde)"""

def ehPosicaoValida(tabuleiro, posicao):
    """Retorna verdadeiro se é possível jogar na posição dada, caso
    contrário, falso"""

def ehVitoria(tabuleiro, simbolo):
    """Retorna verdadeiro se o símbolo recebido forma uma sequência
    vencedora no jogo da velha, caso contrário, falso"""

def trocaTurno(jogador_atual, jogadores, simbolo_atual, simbolos):
    """Retorna uma string e um caractere que correspondem ao nome e
    símbolo do jogador da próxima rodada, respsectivamente"""

def jogada(tabuleiro, jogador):
    """Retorna um inteiro que representa a posição escolhida pelo
    jogador"""
    if jogador == CPU_FACIL:
        return cpuFacilJogada(tabuleiro)
    elif jogador == CPU_DIFICIL:
        return cpuDificilJogada(tabuleiro)
    else:
        return int(input())

def jogoDaVelha(tabuleiro, jogadores, simbolos):
    """Retorna uma string que representa o nome do vencedor do jogo.
    Caso não exista um vencedor, retorna -1"""
    jogador_atual = jogadores[0]
    simbolo_atual = simbolos[0]
    vencedor = -1 # por default, a partida termina em empate
    while podeJogar(tabuleiro):
        mostraTelaJogo(tabuleiro, jogadores, simbolos)
        posicao = jogada(tabuleiro, jogador_atual)
        if ehPosicaoValida(tabuleiro, posicao):
            tabuleiro[posicao] = simbolo_atual
            if ehVitoria(tabuleiro, simbolo_atual):
                vencedor = jogador_atual
            jogador_atual, simbolo_atual = trocaTurno(
                jogador_atual, jogadores, simbolo_atual, simbolos)
        else:
            # quando a interface for criada, isso deve ser trocado
            print("Escolha uma jogada válida") 
    mostraTelaJogo(tabuleiro, jogadores, simbolos)
    return vencedor

def main():
    # EXEMPLO de execução do jogo sem menus, opções, etc
    tabuleiro = 10*[0]
    jogadores = ["Alice", "Bob"]
    simbolos = ["X", "O"]
    vencedor = jogoDaVelha(tabuleiro, jogadores, simbolos)
    if vencedor != -1:
        print(vencedor, "venceu!")
    else:
        print("Empate!")
    exit(0)

if __name__ == "__main__":
    main()
