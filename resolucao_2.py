def rank(v, d):
  r = v - d
  return r


nome = input("Digite seu nome: ")
vitoria = int(input("Qual o numero de vitorias? "))
derrota = int(input("Qual o numero de derrotas? "))

rank(vitoria, derrota)

"""
Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal
"""

if r <= 10:
  nivel = "Ferro"
elif r > 10 and r <= 20:
  nivel = "Bronze"
elif r > 20 and r <= 50:
  nivel = "Prata"
elif r > 50 and r <= 80:
  nivel = "Ouro"
elif r > 80 and r <= 90:
  nivel = "Diamante"
elif r > 90 and r <= 100:
  nivel = "Lendario"
else:
  nivel = "Imortal"

print(f"O Herói tem de saldo de {r} está no nível de {nivel}"
