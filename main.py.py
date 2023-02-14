print("Jose Daniel Cifuentes Carrascosa")
print("1548423")

import os

mi ubicacion = os.getcwd()
if os.path.exists("modulos")
    print("La carpeta ya existe")
else:
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()