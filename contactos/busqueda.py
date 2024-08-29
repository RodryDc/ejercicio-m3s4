from contactos.gestion import lista_contactos

def buscar_contacto(nombre):
    contactos_encontrados = []
    for contacto in lista_contactos:
        if nombre in contacto[0]:
            contactos_encontrados.append(contacto)
    return contactos_encontrados

