import string
import random
import timeit

class USUARIO :
    def __init__(self, NOMBRE, ID, EDAD):
        self.NOMBRE = NOMBRE
        self.ID = ID
        self.EDAD = EDAD
    def __repr__(self):
        return f"usuario ID = {self.ID} | Nombre =  {self.NOMBRE} | Edad = {self.EDAD}"

def creacion(n):
    listusuario = []
    for i in range (1, n+1 ):
        NOMBRE = ''.join(random.choices(string.ascii_letters, k=5))
        EDAD = random.randint(18,70)
        listusuario.append(USUARIO(NOMBRE, i, EDAD))
    return listusuario
usuario = creacion(100000)

def busqlin (listusuario, IDBU):
    for usuario in listusuario:
        if usuario.ID == IDBU:
            return usuario
    return None

def busqBin(listusuario, IDBU):
    izquierda, derecha = 0, len(listusuario) -1
    while izquierda <= derecha:
        media = (izquierda + derecha) //2
        if listusuario[media].ID == IDBU:
            return listusuario[media]
        elif listusuario[media].ID < IDBU:
            izquierda = media + 1
        else:
            derecha = media - 1
    return None

print(f"Los Usuarios aleatorios son: ")
for i in range (100000):
    print(usuario[i])

resultado1 = busqlin(usuario,9)
resultado2 = busqlin(usuario, 9)
print(f"---------------------------------------")
print(f"Resultado de la busqueda Lineal: ")
print(resultado1)
print(f" ")
print(f"Resultado de la busqueda binaria: ")
print(resultado2)
print(f" ")

print(f"Tiempo de busqueda:")
print(f" ")
id = 50000

tiempo_lineal = timeit.timeit(lambda: busqlin(usuario, id), number=1)
print(f"Busqueda Lineal: {tiempo_lineal:.6f} segundos")

tiempo_binaria = timeit.timeit(lambda: busqlin(usuario, id), number=1)
print(f"Busqueda Binaria: {tiempo_binaria:.6f} segundos")
print(f" ")
