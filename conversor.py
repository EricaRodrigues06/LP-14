import os

polegadas = float(input('Escreva o valor em centímetros que deseja converter para polegadas: '))
os.system("clear")

def converter():
  c = polegadas/2.54
  c1 = 6
  return round(c,c1)