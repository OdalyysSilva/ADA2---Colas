class Cola:
    def __init__(self):
        self.cola = [] # Almacenar los elementos de la cola.
        self.contador = 1

    def agregar_cliente(self):  # Añade un cliente a la cola con su número de atención
        cliente = f'c{self.contador}'
        self.cola.append(cliente)
        print(f"Cliente {cliente} agregado al servicio.")
        self.contador += 1

    def atender_cliente(self):  # Atiende al cliente que esté en la cola
        if self.cola:
            cliente_atendido = self.cola.pop(0)
            print(f"Atendiendo al {cliente_atendido}")
        else:
            print("No hay clientes en este servicio.")

    def estado_cola(self):
        return self.cola if self.cola else ["No hay clientes"]

def mostrar(servicios):
    print("\nEstado actual:")
    for numero_servicio, cola in sorted(servicios.items()):
        print(f"Servicio {numero_servicio}: {cola.estado_cola()}", "\n", "-" * 40)

def menu():
    servicios = {}
    print("\nServicios bancarios: \n")
    print("Servicio 1: Apetura de cuentas")
    print("Servicio 2: Depositos")
    print("Servicio 3: Retiros")
    print("Servicio 4: Pretamos")
    print("\nIngrese ¨C¨ para agregar y ¨A¨ para atender clientes, y despues inserte el numero del servicio o ¨S¨ para salir\n")

    while True:
        comando = input("Ingrese el comando: ").upper()

        if comando == "S":
            print("Saliendo del programa.")
            break

        if len(comando) < 2:
            print("Comando inválido. Ingrese 'C' o 'A' seguido del número del servicio.")
            continue

        accion = comando[0]  # 'C' o 'A'
        numero_servicio = comando[2:]  # Número del servicio

        if not numero_servicio.isdigit():
            print("El número de servicio debe ser un número o ponga un espacio entre la letra y el numero.")
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
                
        mostrar(servicios)
menu() # Iniciar el menú del sistema
