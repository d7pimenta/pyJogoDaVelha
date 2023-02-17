# Definindo o tabuleiro vazio
tabuleiro = [' '] * 9

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    print(tabuleiro[0] + '|' + tabuleiro[1] + '|' + tabuleiro[2])
    print('-+-+-')
    print(tabuleiro[3] + '|' + tabuleiro[4] + '|' + tabuleiro[5])
    print('-+-+-')
    print(tabuleiro[6] + '|' + tabuleiro[7] + '|' + tabuleiro[8])

# Função para checar se há um vencedor
def checar_vencedor(simbolo):
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == simbolo:
        return True
    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == simbolo:
        return True
    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == simbolo:
        return True
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == simbolo:
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == simbolo:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == simbolo:
        return True
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == simbolo:
        return True
    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == simbolo:
        return True
    else:
        return False

# Loop principal do jogo
def jogar_jogo():
    jogador_atual = 'X'
    jogando = True
    while jogando:
        exibir_tabuleiro()
        jogada = int(input("Digite a posição que deseja jogar (1-9): ")) - 1
        if tabuleiro[jogada] == ' ':
            tabuleiro[jogada] = jogador_atual
            if checar_vencedor(jogador_atual):
                exibir_tabuleiro()
                print("Parabéns! O jogador " + jogador_atual + " venceu!")
                jogando = False
            elif ' ' not in tabuleiro:
                exibir_tabuleiro()
                print("Empate!")
                jogando = False
            else:
                if jogador_atual == 'X':
                    jogador_atual = 'O'
                else:
                    jogador_atual = 'X'
        else:
            print("Posição ocupada. Tente novamente.")

# Iniciando o jogo
jogar_jogo()