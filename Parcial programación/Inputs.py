def obtener_entero(mensaje, min_val=1, max_val=10):
    """
    Trae un número entero dentro de un rango específico.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        min_val (int): Valor mínimo permitido
        max_val (int): Valor máximo permitido
    
    Returns:
        int: Número válido ingresado por el usuario
    """
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val: #Verifica que el valor esté dentro del rango
                return valor
            print(f"Error: El valor debe estar entre {min_val} y {max_val}")
        except ValueError:
            print("Error: Debe ingresar un número entero válido") #except ValueError captura errores de conversión a entero

def obtener_nombre(mensaje, min_caracteres=3):
    """
    Obtiene un nombre válido (solo letras y espacios, mínimo de caracteres).
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        min_caracteres (int): Cantidad mínima de caracteres requeridos
    
    Returns:
        str: Nombre válido ingresado por el usuario
    """
    while True:
        nombre = input(mensaje).strip()
        if len(nombre) < min_caracteres:
            print(f"Error: El nombre debe tener al menos {min_caracteres} caracteres")
            continue
        
        if all(c.isalpha() or c.isspace() for c in nombre): #Verifica que solo contenga letras y espacios
            return nombre
        print("Error: El nombre solo puede contener letras y espacios")