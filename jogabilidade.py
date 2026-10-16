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

    def monstro(self):

        print("\n----------------------")
        print("Voce encontrou um monstro !")
        print("\n----------------------")

        