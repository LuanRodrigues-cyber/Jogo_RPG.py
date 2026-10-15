import jogador
import missoes

nome = input("Digite o nome do jogador: ")
meu_player = jogador.Player(nome)

print("Bem-vindo, {}! Boa sorte em sua aventura!".format(meu_player.nome))

def verificar_nivel():
     while meu_player.experiencia >= 100:
        meu_player.nivel += 1
        meu_player.experiencia -= 100
        print("Parabéns! Você subiu para o nível {}!".format(meu_player.nivel))

historico_missoes = [] 
def missao_concluida(decisao_missao):
    if decisao_missao == "1":
        historico_missoes.append("Explorar Floresta")
    elif decisao_missao == "2":
        historico_missoes.append("Derrotar um Monstro")
    elif decisao_missao == "3":
        historico_missoes.append("Encontrar um Tesouro")

    meu_player.missoes_concluidas += 1

def menu_jogo():
    decisao = "sim"

    while decisao == "sim":

        print("\nMENU DO JOGADOR!")
        print("1 - Ver status do jogador")
        print("2 - Realizar missão")
        print("3 - Ver histórico de missões")
        print("4 - Descansar")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print ("\nSTATUS DO JOGADOR!")
            print ("NOME: {}".format(meu_player.nome))
            print ("NIVEL: {}".format(meu_player.nivel))
            print ("EXPERIENCIA: {}".format(meu_player.experiencia))
            print ("MOEDAS: {}".format(meu_player.moedas))
            print ("VIDA: {}".format(meu_player.vidas))
            print ("MISSOES CONCLUIDAS: {}".format(meu_player.missoes_concluidas))
            decisao = input("Deseja voltar ao menu? ").lower()

        elif opcao == "2":
            print ("1 - EXPLORAR FLORESTA")
            print ("2 - DERROTAR UM MONSTRO")
            print ("3 - ENCONTRAR UM TESOURO")

            decisao_missao = input("Escolha uma missão: ")

            if decisao_missao == "1":
                print("Você escolheu explorar a floresta!")
                print("Você ganhou {} pontos de experiência e {} moedas!".format(missoes.explorar_floresta_xp, missoes.explorar_floresta_moedas))
                meu_player.experiencia = meu_player.experiencia + missoes.explorar_floresta_xp
                meu_player.moedas = meu_player.moedas + missoes.explorar_floresta_moedas

                verificar_nivel()
                missao_concluida(decisao_missao)
                decisao = input("Deseja voltar ao menu? ").lower()

            elif decisao_missao == "2":
                print("Você escolheu derrotar um monstro!")
                print("Você ganhou {} pontos de experiência e {} moedas!".format(missoes.derrotar_monstro_xp, missoes.derrotar_monstro_moedas))
                meu_player.experiencia = meu_player.experiencia + missoes.derrotar_monstro_xp
                meu_player.moedas = meu_player.moedas + missoes.derrotar_monstro_moedas

                verificar_nivel()
                missao_concluida(decisao_missao)
                decisao = input("Deseja voltar ao menu? ").lower()

            elif decisao_missao == "3":
                print("Você escolheu encontrar um tesouro!")
                print("Você ganhou {} pontos de experiência e {} moedas!".format(missoes.encontrar_tesouro_xp, missoes.encontrar_tesouro_moedas))
                meu_player.experiencia = meu_player.experiencia + missoes.encontrar_tesouro_xp
                meu_player.moedas = meu_player.moedas + missoes.encontrar_tesouro_moedas

                verificar_nivel()
                missao_concluida(decisao_missao)
                decisao = input("Deseja voltar ao menu? ").lower()

        elif opcao == "3":
                    print ("\nHISTORICO DE MISSOES")

                    if len(historico_missoes) == 0:
                        print("Nenhuma missão concluída ainda.")
                    else:   
                        for missao in historico_missoes:
                            print("A missão concluída foi: {}".format(missao))
                            print("Total de missões concluídas: {}".format(meu_player.missoes_concluidas))
                    decisao = input("Deseja voltar ao menu? ").lower() 

        elif opcao == "5":
            decisao = "nao"

    print("Saindo do jogo. Até a próxima!")

menu_jogo()