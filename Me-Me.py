# primero definimos una lista donde se guardan los eventos
agenda=[]

# hacemos una función para mostrar el menú
def mostrarMenu():
    print("-Agregar evento \n-Ver eventos\n-buscar evento\n-editar evento\n-salir")
    

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
            encotrado=True
            break
        i+=1 
    
    if not encontrado:
        print("no se encontró ningún evento con ese nombre.\n")


#Funcion principal que ejecuta el programa
def ejecutarAgenda():
    while True:
       print("BIENVENIDO A LA AGENDA ME-ME")
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
        elif opcion == "salir":
            print("Cerrando me-me")
            break
        else:
            print("opción no válida, por favor intenta de nuevo\n")

#Funcion main que inicia el programa
def main():
    print("bienvenido a la agenda de eventos")
    ejecutarAgenda()

main()
