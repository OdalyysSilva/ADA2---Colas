class Cola:
    def __init__(self):
        self.valor = []

    def encolar(self, item):
        self.valor.append(item)

    def desencolar(self):
        return self.valor.pop(0) if self.valor else None

def suma(cola1, cola2):
    print("\nCola 1   Cola 2   Suma de la cola 1 y 2")
    while cola1.valor and cola2.valor:
        elemento1 = cola1.desencolar()
        elemento2 = cola2.desencolar() # Suma los elementos desencolados
        cola3 = elemento1 + elemento2
        print(f"  {elemento1:<8} {elemento2:<9} {cola3:<5}\n")

def definir(cola, nomcola, n):
    for _ in range(n):
        cola.encolar(int(input(f"Inserta un número para la {nomcola}: ")))

n = int(input("\nInserta el numero de elementos para las colas: "))
# Crea dos instancias de la clase Cola (cola1 y cola2)
cola1, cola2 = Cola(), Cola()
definir(cola1, "Cola 1", n)
definir(cola2, "Cola 2", n)

suma(cola1, cola2)
