import time

def telaMenu():
    opcao = 1
    while 1:
        if opcao > 0 and opcao < 5:
            print('Jogo da Velha')
            print('1 - Jogar')
            print('2 - Instruções')
            print('3 - Créditos')
            print('4 - Sair')
            opcao = int(input())
            if opcao > 0 and opcao < 5:
                break
            else:
                print('Opção Inválida. Tente novamente')
    return opcao

def telaModoDeJogo():
    print('1 - 1 jogador')
    print('2 - 2 jogadores')
    print('3 - Retornar')
    opcao = int(input())
    if opcao == 1:
        print('1 - IA iniciante')
        print('2 - IA hard')
        print('3 - Retornar')
        opcao = int(input())
        if opcao == 1:
            print('contra bot iniciante')
            # executa jogo contra bot iniciante
        elif opcao == 2:
            print('contra bot hard')
            # executa jogo contra bot hard
        elif opcao == 3:
            telaModoDeJogo()
    elif opcao == 2:
        print('executa pvp')
        # executar jogo pvp (dois jogadores)
    elif opcao == 3:
        telaMenu()

def telaInstrucao():
    print('O tabuleiro é uma matriz de três linhas por três colunas. Dois jogadores escolhem uma marcação cada um, geralmente um círculo (O) e um xis (X).')
    print(' Os jogadores jogam alternadamente, uma marcação por vez, numa lacuna que esteja vazia.')
    time.sleep(10)

def main():
    opcao = telaMenu()
    if opcao == 1:
        telaModoDeJogo()
    elif opcao == 2:
        telaInstrucao()
        main()
    elif opcao == 3: 
        print('apresenta creditos')
        main()
    elif opcao == 4:
        exit(1)

if __name__ == "__main__":
    while 1:
        main()
