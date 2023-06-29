import random
from itertools import product
def palabra(lista):
  aleatorio = random.choice(lista)
  return aleatorio

def formal(palabra):
  return [palabra.lower(), palabra.upper(), palabra.capitalize()]
  

def combinador_palabras_clave(palabras_clave):
    combinaciones = []
    for j in range(1,2000):
      rango = list(range(0,len(palabras_clave)))
      random.shuffle(rango)
      lista = list(map(lambda y: palabra(palabras_clave[y]),rango[0: random.randint(2, 4)]))
      contraseña = "".join(lista)
      if contraseña in combinaciones:
        continue
      if contraseña[0] in caracter:
        continue
      if contraseña[len(contraseña)-1] in caracter:
        continue
      if len(contraseña)<6:
        continue
      combinaciones.append(contraseña)
      print(contraseña)
        
    

primer_nombre= formal("Luis")
segundo_nombre= formal("ferNando")
primer_apellido= formal("HuarcaYa")
segundo_apellido= formal("DeLaCruz")
dia=['08']
mes=['09']
año=['1999']
caracter=['.','-']
simbolo=['@']

palabras_clave=[primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, dia, mes, año, caracter, simbolo]
contraseñas = combinador_palabras_clave(palabras_clave)