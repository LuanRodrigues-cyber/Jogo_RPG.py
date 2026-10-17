import jogador
import missoes
from jogabilidade import Explorar_Floresta, Encontrar_Tesouro, Derrotar_Monstro

nome = input("Digite o nome do jogador: ")
meu_player = jogador.Player(nome)
floresta = Explorar_Floresta(meu_player)
tesouro = Encontrar_Tesouro(meu_player)
monstro = Derrotar_Monstro(meu_player)

print("Bem-vindo, {}! Boa sorte em sua aventura!".format(meu_player.nome))

def verificar_nivel():
     while meu_player.experiencia >= 100:
        meu_player.nivel += 1
        meu_player.experiencia -= 100
        print("\n----------------------")
        print("Parabéns! Você subiu para o nível {}!".format(meu_player.nivel))

def verificar_estamina():
    meu_player.estamina <= 0

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
            print ("ESTAMINA: {}".format(meu_player.estamina))
            print ("MISSOES CONCLUIDAS: {}".format(meu_player.missoes_concluidas))
            decisao = input("Deseja voltar ao menu? ").lower()

        elif opcao == "2":

            print ("1 - EXPLORAR FLORESTA")
            print ("2 - DERROTAR UM MONSTRO")
            print ("3 - ENCONTRAR UM TESOURO")

            decisao_missao = input("Escolha uma missão: ")

            if decisao_missao == "1":

                verificar_estamina()
                if meu_player.estamina < 20:
                    print("\n----------------------")
                    print("Voce nao tem estamina suficiente para realizar essa missao! Descanse para se recuperar.") 
                else:
                    meu_player.estamina -= 20

                    print("\n----------------------")
                    print("Você escolheu explorar a floresta!")
                    floresta.floresta()

                    missao_concluida(decisao_missao)
                    decisao = input("Deseja voltar ao menu? ").lower()

            elif decisao_missao == "2":

                verificar_estamina()
                if meu_player.estamina < 20:
                    print("Voce nao tem estamina suficiente para realizar essa missao!") 
                else:
                    meu_player.estamina -= 20
                    resultado = monstro.combate()

                    if resultado:
                        verificar_nivel()
                        missao_concluida(decisao_missao)
                    decisao = input("Deseja voltar ao menu? ").lower()

            elif decisao_missao == "3":

                verificar_estamina()
                if meu_player.estamina < 20:
                    print("Voce nao tem estamina suficiente para realizar essa missao!") 
                else:
                    meu_player.estamina -= 20
                    tesouro.tesouro()

                    verificar_nivel()
                    missao_concluida(decisao_missao)
                    decisao = input("Deseja voltar ao menu? ").lower()

        elif opcao == "3":
                    print ("\nHISTORICO DE MISSOES")

                    if len(historico_missoes) == 0:
                        print("Nenhuma missão concluída ainda.")
                    else:
                        print ("\nAs missoes concluidadas foram: ")   
                        for i, missao in enumerate(historico_missoes, start=1):
                            print(" {} - {}".format(i, missao))

                        print("Total de missões concluídas: {}".format(meu_player.missoes_concluidas))
                    decisao = input("Deseja voltar ao menu? ").lower()

        elif opcao == "4":

            print("Você escolheu descansar!")
            meu_player.estamina += 20
            if meu_player.estamina > 100:
                meu_player.estamina = 100

            meu_player.vidas += 1
            if meu_player.vidas > 5:
                meu_player.vidas = 5
            decisao = input("Deseja voltar ao menu? ").lower()

        elif opcao == "5":
            decisao = "nao"

    print("Saindo do jogo. Até a próxima!")

menu_jogo()