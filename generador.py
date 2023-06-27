from itertools import product

def combinador_palabras_clave(palabras_clave):
    combinaciones = []
    for longitud_combinacion in range(1, 5):
        for combinacion in product(palabras_clave, repeat=longitud_combinacion):
            combinaciones.append(combinacion)
    return combinaciones

# Ejemplo de uso
palabras_clave = ['JANINA', 'YANINA','ADDY','SERNAQUE','VILLEGAS',
                  'Janina','Yanina', 'Addy','Sernaque', 'Villegas',
                  'janina','yanina','addy', 'sernaque','villegas'
                  '08','8','05','5','2001','.']
resultados = combinador_palabras_clave(palabras_clave)
print(resultados)
