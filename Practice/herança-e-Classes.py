class Restaurante:

    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.servidos = 0


    def descrever(self):
        print(f"O restaurante chama-se {self.nome} e o tipo de cozinha é {self.tipo_cozinha}")

    def abrirRestaurante(self):
        print(f"O restaurante {self.nome} está aberto")

    def definir_servidos(self, numero):
        if numero > self.servidos:
            self.servidos = numero
        else:
            print("Estas a adulterar o sistema.....")

restaurante1 = Restaurante("Saaaa", "Unecas")
restaurante1.definir_servidos(10)
restaurante1.definir_servidos(20)
print(f"Numero de clientes servidos {restaurante1.servidos}")


class Geladaria(Restaurante):

    def __init__(self, sabores):
        super().__init__("Geladaria", "Gelados")
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Os sabores disponíveis são {self.sabores}:")
       

geladaria1 = Geladaria(["Chocolate", "Morango", "Creme"])
geladaria1.mostrar_sabores()
