- el programa nos permitira realizar ciertas funciones como, buscar usuarios de manera lineal y binarias así mismo la creacion de 10000 usuarios totalmente random

en esta parte del codigo tenemos el codigo que nos servira para la 
creacion de los 100000 usuarios

```python
def creacion(n):
    listusuario = []
    for i in range (1, n+1 ):
        NOMBRE = ''.join(random.choices(string.ascii_letters, k=5))
        EDAD = random.randint(18,70)
        listusuario.append(USUARIO(NOMBRE, i, EDAD))
    return listusuario
usuario = creacion(100000)
```


En este esta parte esta la opcion de tanto la busqueda lineal como la busqueda binario 
```python
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
```

se impremen los resultados 
```python
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

```
