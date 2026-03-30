# Classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        # Estrutura de decisão para definir o tipo de ataque
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")


# Criando objetos (instâncias)
heroi1 = Heroi("Gandalf", 150, "mago")
heroi2 = Heroi("Aragorn", 87, "guerreiro")
heroi3 = Heroi("Liu Kang", 30, "monge")
heroi4 = Heroi("Naruto", 17, "ninja")

# Chamando o método atacar
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
