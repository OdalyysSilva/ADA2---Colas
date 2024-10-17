class Cola:
    def __init__(self):
        self.valor = []

    def encolar(self, item):
        self.valor.append(item)

    def desencolar(self):
        return self.valor.pop(0) if self.valor else None 
    # Este método elimina y devuelve el primer elemento de la cola.

    def mostrar(self): 
        # Este método devuelve una representación de la cola y si la cola está vacía, devuelve la palabra "vacía".
        return ', '.join(map(str, self.valor)) if self.valor else 'vacía'

def imprimir_colas(cola1, cola2):
    max_len = max(len(cola1.valor), len(cola2.valor))
    print("\nCola 1   Cola 2")
    for i in range(max_len):
        valor_cola1 = cola1.valor[i] if i < len(cola1.valor) else ''
        valor_cola2 = cola2.valor[i] if i < len(cola2.valor) else ''
        print(f"  {valor_cola1:<7} {valor_cola2:<7}")

def suma(cola1, cola2):
    resultado = []

    imprimir_colas(cola1, cola2)
    print()
    while cola1.valor and cola2.valor: # Desencolar y mostrar el resultado parcial.
        elemento1 = cola1.desencolar()
        elemento2 = cola2.desencolar()

        suma_elementos = elemento1 + elemento2
        resultado.append(suma_elementos)

        # Mostrar el estado de las colas después de cada desencolado.
        print(f"\nResultado de la suma al tomar el primer elemento de cada cola: {resultado}\n")
        imprimir_colas(cola1, cola2)

    print(f"\nResultados: {resultado}") # Mostrar que las colas están vacías al final.
    print(f"Estado final de Cola 1: [{cola1.mostrar()}]")
    print(f"Estado final de Cola 2: [{cola2.mostrar()}]")

def definir(cola, nomcola, n):
    for _ in range(n):
        cola.encolar(int(input(f"Inserta un número para la {nomcola}: ")))

n = int(input("\nInserta el número de elementos para las colas: "))

cola1, cola2 = Cola(), Cola() # Crea dos instancias de la clase Cola (cola1 y cola2).
definir(cola1, "Cola 1", n)
definir(cola2, "Cola 2", n)

suma(cola1, cola2)