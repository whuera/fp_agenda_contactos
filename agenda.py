
# Definir la lista para almacenar los contactos
"""
Agenda de Contactos
Este módulo proporciona una agenda de contactos simple que permite añadir, buscar, eliminar y mostrar contactos.
Funciones:
- añadir_contacto(nombre, telefono, email): Añade un nuevo contacto a la agenda.
- buscar_contacto(nombre): Busca un contacto por nombre en la agenda.
- eliminar_contacto(nombre): Elimina un contacto por nombre de la agenda.
- mostrar_contactos(): Muestra todos los contactos en la agenda en orden alfabético.
- menu(): Muestra el menú principal para interactuar con el usuario.
Ejemplo de uso:
    python agenda.py
Notas:
- Los contactos se almacenan en una lista llamada 'agenda'.
- Cada contacto es un diccionario con las claves 'nombre', 'telefono' y 'email'.
"""
agenda = []

# Función para añadir un nuevo contacto
def añadir_contacto(nombre, telefono, email):
    contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    agenda.append(contacto)
    print(f"Contacto '{nombre}' añadido correctamente.")

# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            return
    print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

# Función para eliminar un contacto por nombre
def eliminar_contacto(nombre):
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre.lower():
            agenda.remove(contacto)
            print(f"Contacto '{nombre}' eliminado correctamente.")
            return
    print(f"No se encontró ningún contacto con el nombre '{nombre}' para eliminar.")

# Función para mostrar todos los contactos en orden alfabético
def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.")
        return
    
    # Ordenar la lista de contactos por nombre
    contactos_ordenados = sorted(agenda, key=lambda x: x['nombre'].lower())
    
    print("Lista de contactos:")
    for contacto in contactos_ordenados:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

# Función principal para interactuar con el usuario
def menu():
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            añadir_contacto(nombre, telefono, email)
        
        elif opcion == '2':
            nombre = input("Introduce el nombre a buscar: ")
            buscar_contacto(nombre)
        
        elif opcion == '3':
            nombre = input("Introduce el nombre a eliminar: ")
            eliminar_contacto(nombre)
        
        elif opcion == '4':
            mostrar_contactos()
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 5.")

# Ejecutar el menú principal

if __name__ == "__main__":
    menu()