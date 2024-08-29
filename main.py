'''
Integrantes:
Rodrigo Donoso Caceres
Marco Yañez Olivares
Yuri Urzua
Luis Gonzalez Castro.
'''

from contactos import gestion,busqueda

def listar_contactos():
    print("Todos los contactos:")
    for contacto in gestion.lista_contactos:
        print(f"Nombre:{contacto[0]}, Email: {contacto[1]}")

def nuevo_contacto():
    nombre = input("Ingresa el nombre del nuevo contacto: ")
    email = input("Ingresa el email del nuevo contacto: ")
    gestion.agregar_contacto(nombre,email)
    print(f"Contacto {nombre} agregado exitosamente",end="\n")
          
def buscar_contacto():
    nombre_buscado = input("Ingresa el nombre a buscar: ")
    contactos_encontrados = busqueda.buscar_contacto(nombre_buscado)    
    for contacto in contactos_encontrados:
        print(f"Nombre:{contacto[0]}, Email: {contacto[1]}")  

print("\n--- Menú Principal ---")
print("1. Opción 1: Listar Contactos")
print("2. Opción 2: Nuevo Contacto")
print("3. Opción 3: Buscar Contacto")
print("4. Opción 4: Salir")
    
opcion = int(input("Selecciona una opción 1 al 4: "))

while (opcion !=4):
    if (opcion == 1):
        listar_contactos()
    elif (opcion == 2):
        nuevo_contacto()
    elif (opcion == 3):
        buscar_contacto()
    else:
        print("Opcion no válida")
    print("\n--- Menú Principal ---")
    print("1. Opción 1: Listar Contactos")
    print("2. Opción 2: Nuevo Contacto")
    print("3. Opción 3: Buscar Contacto")
    print("4. Opción 4: Salir")
    
    opcion = int(input("Selecciona una opción 1 al 4: "))

#listar_contactos()
#nuevo_contacto()
#print("Contactos Actualizados")
#listar_contactos()



