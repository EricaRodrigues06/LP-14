from conversor import *

conversor = converter()

def arquivo():
  file = open('converter.txt', 'a+')
  file.write('O valor digitado foi: {} em centímetros \nQue equivale ao valor {} em polegadas.\n' .format(polegadas,conversor))
  file.seek(0,0)
  file.read()
  print(file.read())
  file.close()

arquivo()