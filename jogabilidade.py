import random

class Explorar_Floresta:
    def __init__(self, player):
        self.player = player

    def floresta(self):
        
        print ("Voce entrou na floresta")

        evento = random.choice(["Voce foi atacado por um lobo!",
                                "Voce encontrou comida para sobreviver!",
                                "Voce encontrou um tesouro escondido!",
                                "Voce nao encontrou nada de interessante!"])
        print(evento)

        if evento == "Voce foi atacado por um lobo!":
            print("\n----------------------")
            self.player.experiencia += 10
            print("Voce nao ganhou nenhuma moeda")
            print("\n----------------------")
            self.player.vidas -= 1
            print('Voce perdeu uma vida, descanse para recuperar sua vida!')

        elif evento == "Voce encontrou comida para sobreviver!":
            print("\n----------------------")

            venda = input("Voce deseja vender a comida? ").lower()
            print("\n----------------------")
            if venda == "sim":
                self.player.moedas += 20
                print ('Voce vendeu a comida e ganhou 20 moedas')
            else:
                self.player.estamina += 20

                if self.player.estamina > 100:
                    self.player.estamina = 100
                print("\n----------------------")
                print('Voce comeu e recuperou 20 de estamina que perdeu explorando a floresta!')

        elif evento == "Voce encontrou um tesouro escondido!":
            print("\n----------------------")
            self.player.experiencia += 30
            self.player.moedas += 50
            print('Voce encontrou um tesouro escondido !! Ganhou 50 moedas e 30 de experiencia!')

        else:
            print("\n----------------------")
            print('Voce nao encontrou nada de interessante na floresta! E perdeu estamina')

            self.player.estamina -= 20
            if self.player.estamina < 0:
                self.player.estamina = 0

class Derrotar_Monstro:
    def __init__(self, player):
        self.player = player

    def combate(self):

        vida_monstro = 3

        print("\n----------------------")
        print("Voce encontrou um monstro!")
        print("Vidas do monstro: {}".format(vida_monstro))
        print("Suas vidas: {}".format(self.player.vidas))
        print("----------------------")

        while vida_monstro > 0 and self.player.vidas > 0:

            print("\n1 - Atacar o monstro")
            print("2 - Tentar fugir")

            decisao = input("O que deseja fazer? ")

            if decisao == "1":
                dano = random.randint(1, 2)
                vida_monstro -= dano

                if vida_monstro < 0:
                    vida_monstro = 0

                print("\nVoce atacou o monstro!")
                print("O monstro perdeu {} vida(s).".format(dano))
                print("Vidas restantes do monstro: {}".format(vida_monstro))

                if vida_monstro > 0:
                    print("\nO monstro contra-atacou!")
                    self.player.vidas -= 1

                    if self.player.vidas < 0:
                        self.player.vidas = 0

                    print("Voce perdeu uma vida!")
                    print("Suas vidas restantes: {}".format(self.player.vidas))

            elif decisao == "2":
                print("Voce fugiu do combate!")
                return False

            else:
                print("Opcao invalida! Escolha 1 ou 2.")
                continue

        if vida_monstro == 0:
            print("\nVoce derrotou o monstro!")
            self.player.experiencia += 50
            self.player.moedas += 40

            print("Voce ganhou 50 de experiencia e 40 moedas!")
            return True

        print("\nVoce ficou sem vidas e perdeu o combate!")
        return False

class Encontrar_Tesouro:
    def __init__(self, player):
        self.player = player

    def tesouro(self):

        print("\n----------------------")
        print("Em busca do tesouro perdido!!")
        print("\n----------------------")

        print("PROCURANDO TESOURO ...")
        print("PROCURANDO TESOURO ...")
        print("PROCURANDO TESOURO ...")
        print("VOCE ENCONTROU O TESOURO, POREM TERA QUE RESOLVER UMA PEGUNTA PARA PEGA-LO !!")
        print("\n----------------------")

        evento = random.choice (["Um produto custa R$ 200. Primeiro, seu preço aumenta 20% e, depois, diminui 20% sobre o novo preço. Qual é o preço final?",
                                "Na frase “Embora estivesse cansado, Pedro continuou estudando”, a palavra “embora” expressa ideia de: ", 
                                "Qual é o órgão responsável por bombear o sangue para todo o corpo humano?",
                                "Uma planta ficou durante vários dias em um armário completamente fechado, sem luz, mas recebendo água. Qual processo será diretamente prejudicado pela falta de luz?",
                                "Qual alternativa apresenta uma característica do feudalismo europeu durante a Idade Média?"
                                ])

        print(evento)

        if evento == "Um produto custa R$ 200. Primeiro, seu preço aumenta 20% e, depois, diminui 20% sobre o novo preço. Qual é o preço final?":
            resposta = int(input("QUAL A SUA RESPOSTA? "))
            if resposta == 192:
                print("Resposta certa")

                self.player.experiencia += 60
                self.player.moedas += 100                    
            else:
                print("Resposta incorreta")

                self.player.experiencia += 30
                print ("Voce nao ganhou nenhuma moeda")

        elif evento == "Na frase “Embora estivesse cansado, Pedro continuou estudando”, a palavra “embora” expressa ideia de: ":
            print("A) CAUSA")
            print("B) CONCLUSAO")
            print("C) CONCESSAO")
            print("D) CONDICAO")

            resposta = input("QUAL A SUA RESPOSTA? ").lower()
            if resposta == "c":
                print("Resposta certa")

                self.player.experiencia += 60
                self.player.moedas += 100
            else:
                print("Resposta incorreta")

                self.player.experiencia += 30
                print ("Voce nao ganhou nenhuma moeda")

        elif evento == "Qual é o órgão responsável por bombear o sangue para todo o corpo humano?":

            resposta = input("QUAL A SUA RESPOSTA? ").lower()
            if resposta == "coracao" or resposta == "coração":
                print("Resposta certa")

                self.player.experiencia += 60
                self.player.moedas += 100
            else:
                print("Resposta incorreta")

                self.player.experiencia += 30
                print ("Voce nao ganhou nenhuma moeda")

        elif evento == "Uma planta ficou durante vários dias em um armário completamente fechado, sem luz, mas recebendo água. Qual processo será diretamente prejudicado pela falta de luz?":
            print("A) RESPIRACAO CELULAR")
            print("B) FOTOSSINTESE")
            print("C) ABSORCAO DE AGUAS PELAS RAIZES")
            print("D) GERMINACAO DE TODAS AS SEMENTES, NECESSARIAMENTE")

            resposta = input("QUAL A SUA RESPOSTA? ").lower()
            if resposta == "b":
                print("Resposta certa")

                self.player.experiencia += 60
                self.player.moedas += 100
            else:
                print("Resposta incorreta")

                self.player.experiencia += 30
                print ("Voce nao ganhou nenhuma moeda")

        elif evento == "Qual alternativa apresenta uma característica do feudalismo europeu durante a Idade Média?":
            print("A) PREDOMINIO DO TRABALHO INDUSTRIAL.")
            print("B) ECONOMIA PRINCIPALMENTE AGRARIA E RELACOES DE DEPENDENCIA ENTRE SENHORES E SERVOS.")
            print("C) DEMOCRACIA REPRESENTATIVA UNIVERSAL")
            print("D) USO GENERALIZADO DE FABRICAS MOVIDAS A ELETRICIDADE")

            resposta = input("QUAL A SUA RESPOSTA? ").lower()
            if resposta == "b":
                print("Resposta certa")

                self.player.experiencia += 60
                self.player.moedas += 100
            else:
                print("Resposta incorreta")

                self.player.experiencia += 30
                print ("Voce nao ganhou nenhuma moeda")
