# primero definimos una lista donde se guardan los eventos
agenda=[]

# hacemos una función para mostrar el menú
def mostrarMenu():
    print("-Agregar evento \n-Ver eventos\n-buscar evento\n-editar evento\n-eliminar evento\n-prueba agenda\n-salir")
    

# funcion para agregar un evento
def agregarEvento():
    nombre=input("nombre del evento: ")
    fecha=input("fecha (DD/MM/AAAA): ")
    hora=input("hora (hh:mm): ")
    agenda.append([nombre, fecha, hora])
    print("evento agregado correctamente\n")

# funcion para mostrar todos los eventos
def verEventos():
    if len(agenda)==0:
        print("no hay eventos en la agenda\n")
    else:
        for evento in agenda:
            print("evento:", evento[0], "| Fecha:", evento[1], "| Hora:", evento[2])
        print("")

# funcion para buscar eventos por nombre o fecha
def buscarEvento():
    criterio=input("buscar por (nombre/fecha): ")
    encontrado=False
    if criterio=="nombre":
        busqueda=input("introduce el nombre del evento: ")
        for evento in agenda:
            if evento[0] == busqueda:
                print("evento encontrado:",evento)
                encontrado = True
    elif criterio == "fecha":
        busqueda=input("introduce la fecha (DD/MM/AAAA): ")
        for evento in agenda:
            if evento[1]==busqueda:
                print("evento encontrado:",evento)
                encontrado=True
    if not encontrado:
        print("no se encontraron eventos con ese criterio\n") #agrego saltos de linea para la estetica

# funcion para editar el evento que elijas
def editarEvento():
    busqueda=input("Introduce el nombre del evento a editar: ").strip().lower()
    encontrado=False
    i=0
    for evento in agenda:
        if evento[0].strip().lower() == busqueda:
            print("evento encontrado: ", evento)
            nuevonombre=input("nuevo nombre del evento (si quieres cambiar otra cosa dejalo en blanco): ").strip()
            nuevafecha=input("nueva fecha (si quieres cambiar otra cosa dejalo en blanco): ").strip()
            nuevahora=input("nueva hora (deja en blanco para no cambiar): ").strip()
            if nuevonombre:
                agenda[i][0]=nuevonombre
            if nuevafecha:
                agenda[i][1]=nuevafecha
            if nuevahora:
                agenda[i][2]=nuevahora

            print("evento actualizado: ",agenda)
            encontrado=True
            break
        i+=1 
    
    if not encontrado:
        print("no se encontró ningún evento con ese nombre.\n")

# funcion para eliminar un evento
def eliminarEvento():
    busqueda=input("Introduce el nombre del evento a eliminar: ").strip().lower()
    encontrado=False
    for evento in agenda:
        if busqueda in evento[0].lower():  # Convertir solo el nombre del evento a minúsculas
            print("Evento encontrado: ",evento)
            confirmacion = input("¿Estás seguro de que deseas eliminar este evento? (s/n): ").strip().lower()
            if confirmacion == "s":
                agenda.remove(evento)
                print("Evento eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún evento con ese nombre.\n")

def pruebaAgenda():
    print("Comenzando prueba completa...")

    # Agregar eventos
    print("\n--- Agregar Eventos ---")
    agenda.append(["Reunión", "16/10/2024", "10:00"])
    print("Evento 'Reunión' agregado correctamente.")
    agenda.append(["Cumpleaños", "17/10/2024", "18:00"])
    print("Evento 'Cumpleaños' agregado correctamente.")

    # Mostrar todos los eventos
    print("\n--- Ver Eventos ---")
    verEventos()

    # Buscar evento por nombre
    print("\n--- Buscar Evento por Nombre 'Reunión' ---")
    encontrado = False
    for evento in agenda:
        if evento[0].lower() == "reunión":
            print("Evento encontrado: ", evento)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el evento 'Reunión'.")

    # Buscar evento por nombre inexistente
    print("\n--- Buscar Evento por Nombre 'Viaje' (inexistente) ---")
    encontrado = False
    for evento in agenda:
        if evento[0].lower() == "viaje":
            print("Evento encontrado: ",evento)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el evento 'Viaje'.")

    # Buscar evento por fecha
    print("\n--- Buscar Evento por Fecha '17/10/2024' ---")
    encontrado = False
    for evento in agenda:
        if evento[1] == "17/10/2024":
            print("Evento encontrado: ",evento)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún evento con la fecha '17/10/2024'.")

    # Buscar evento por fecha inexistente
    print("\n--- Buscar Evento por Fecha '18/10/2024' (inexistente) ---")
    encontrado = False
    for evento in agenda:
        if evento[1] == "18/10/2024":
            print("Evento encontrado: ",evento)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún evento con la fecha '18/10/2024'.")

    # Editar evento
    print("\n--- Editar Evento 'Reunión' ---")
    encontrado = False
    i = 0
    for evento in agenda:
        if evento[0].strip().lower() == "reunión":
            print("Evento encontrado: ",evento)
            agenda[i][0] = "Reunión de trabajo"  
            agenda[i][2] = "11:00" 
            print("Evento actualizado:",agenda[i])
            encontrado = True
            break
        i += 1
    if not encontrado:
        print("No se encontró el evento 'Reunión' para editar.")

    # Mostrar eventos después de la edición
    print("\n--- Ver Eventos Después de la Edición ---")
    verEventos()

    # Eliminar evento
    print("\n--- Eliminar Evento 'Cumpleaños' ---")
    encontrado = False
    for evento in agenda:
        if "cumpleaños" == evento[0].lower():
            agenda.remove(evento)
            print("Evento 'Cumpleaños' eliminado correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el evento 'Cumpleaños' para eliminar.")

    # Mostrar eventos después de la eliminación
    print("\n--- Ver Eventos Después de la Eliminación ---")
    verEventos()

    print("Prueba completa finalizada.")

# funcion principal que ejecuta el programa
def ejecutarAgenda():
    while True:
        mostrarMenu()
        opcion=str(input("selecciona(escribe) una opción: ")).strip().lower()
        if opcion == "agregar evento" or opcion == "agregar":
            agregarEvento()
        elif opcion == "ver evento" or opcion == "ver":
            verEventos()
        elif opcion == "buscar evento" or opcion == "buscar":
            buscarEvento()
        elif opcion == "editar evento" or opcion =="editar":
            editarEvento()
        elif opcion == "eliminar evento" or opcion == "eliminar":
            eliminarEvento()
        elif opcion == "prueba funciones" or opcion == "prueba":
            pruebaAgenda()
        elif opcion == "salir":
            print("Cerrando me-me")
            break
        else:
            print("opción no válida, por favor intenta de nuevo\n")

# funcion main que inicia el programa
def main():
    print("bienvenido a la agenda de eventos")
    ejecutarAgenda()

main()
