class Cola:
    def __init__(self):
        self.cola = [] 
        self.contador = 1
 
    def agregar_cliente(self): # Añade un cliente  a la cola con su número de atención
        self.cola.append(self.contador)
        print(f"Cliente agregado a la cola con número {self.contador}")
        self.contador += 1

    def atender_cliente(self): # Atiende al cliente que esté en la cola   
        if self.cola:
            numero_atendido = self.cola.pop(0)
            print(f"Atendiendo al cliente con número {numero_atendido}")
        else:
            print("No hay clientes en la cola para este servicio.")

# Diccionario para almacenar las colas según cuantos servicios se hicieron
servicios = {}

print("\n¨C¨ para agregar y ¨A¨ para atender clientes, S para salir, despues inserte el numero de servicio...\n")
def menu():
    while True:
        comando = input("Ingrese un comando: ").upper()
        if comando == "S":
            print("Saliendo del sistema.")
            break
        
        if len(comando) < 2:
            print("Comando inválido. Ingrese C o A seguido del número de servicio.")
            continue

        accion = comando[0]  # C o A
        numero_servicio = comando[1:]  # Número del servicio

        if not numero_servicio.isdigit():
            print("El número de servicio debe ser un número.")
            continue

        numero_servicio = int(numero_servicio)

        if accion == "C":  # Agrega un cliente a la cola
            if numero_servicio not in servicios:
                servicios[numero_servicio] = Cola() 
            servicios[numero_servicio].agregar_cliente()

        elif accion == "A":  # Atiende un cliente
            if numero_servicio in servicios:
                servicios[numero_servicio].atender_cliente()
            else:
                print(f"No hay una cola creada para el servicio {numero_servicio}.")
        else:
            print("Comando no reconocido. Use C para agregar cliente o A para atender cliente.")
menu()
