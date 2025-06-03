def obtener_entero(mensaje):
    """
    Solicita al usuario un número entero con validación.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    
    Returns:
        int: Número entero ingresado por el usuario
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Ingrese un número entero válido.") #except ValueError captura errores de conversión a entero

def calcular_promedio(puntajes):
    """
    Calcula el promedio de una lista de puntajes.
    
    Args:
        puntajes (list): Lista de puntajes
    
    Returns:
        float: Promedio de los puntajes
    """
    total = 0
    contador = 0
    for puntaje in puntajes:
        total += puntaje
        contador += 1
    return total / contador if contador > 0 else 0

def obtener_nombre(mensaje):
    """
    Solicita al usuario un nombre válido (no vacío ni con numero).
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    
    Returns:
        str: Nombre ingresado por el usuario
    """
    while True:
        nombre = input(mensaje).strip() #eliminar esoacios
        if nombre and nombre.isalpha(): #isalpha() verifica que solo contenga letras
            return nombre
        print("Ingrese un nombre válido (solo letras, sin números ni espacios).")

def cargar_participantes():
    """
    Carga los nombres de 5 participantes con validación.
    
    Returns:
        list: Lista de nombres de participantes
    """
    participantes = []
    for i in range(5):
        nombre = obtener_nombre(f"Ingrese el nombre del participante {i+1}: ") #i+1 para numerar desde 1
        participantes = participantes + [nombre]  # Concatenación en lugar de append
    return participantes

def cargar_puntuaciones(participantes):
    """
    Carga las puntuaciones de los 3 jurados para cada participante.
    Las puntuaciones deben estar entre 1 y 10.
    
    Args:
        participantes (list): Lista de nombres de participantes
    
    Returns:
        list: Lista de diccionarios con nombre y puntuaciones
    """
    puntuaciones = []  # Inicia vacía
    for participante in participantes:
        print(f"\nPuntuaciones para {participante}:")
        while True:
            jurado1 = obtener_entero("  Jurado 1: ")
            if 1 <= jurado1 <= 10:
                break
            print("La puntuación debe estar entre 1 y 10.")
        while True:
            jurado2 = obtener_entero("  Jurado 2: ")
            if 1 <= jurado2 <= 10:
                break
            print("La puntuación debe estar entre 1 y 10.")
        while True:
            jurado3 = obtener_entero("  Jurado 3: ")
            if 1 <= jurado3 <= 10:
                break
            print("La puntuación debe estar entre 1 y 10.")
        
        nuevo_participante = {
            'nombre': participante,
            'jurado1': jurado1,
            'jurado2': jurado2,
            'jurado3': jurado3,
            'promedio': calcular_promedio([jurado1, jurado2, jurado3]) #Tdoo cargado en una sola línea
        }
        puntuaciones = puntuaciones + [nuevo_participante]  # Concatenación en lugar de append
    return puntuaciones

def mostrar_puntuaciones(puntuaciones):
    """
    Muestra las puntuaciones de todos los participantes.
    
    Args:
        puntuaciones (list): Lista de diccionarios con datos de participantes
    """
    print("\n--- Puntuaciones de los participantes ---")
    for p in puntuaciones:
        print(f"\nNOMBRE PARTICIPANTE: {p['nombre']}")
        print(f"PUNTAJE JURADO 1: {p['jurado1']}")
        print(f"PUNTAJE JURADO 2: {p['jurado2']}")
        print(f"PUNTAJE JURADO 3: {p['jurado3']}")
        print(f"PUNTAJE PROMEDIO: {p['promedio']:.2f}/10") #Redondea a dos decimales

def filtrar_por_promedio(puntuaciones, minimo):
    """
    Filtra participantes con promedio mayor al valor especificado.
    
    Args:
        puntuaciones (list): Lista de diccionarios con datos de participantes
        minimo (float): Valor mínimo del promedio para filtrar
    
    Returns:
        list: Lista filtrada de participantes
    """
    filtrados = []
    for p in puntuaciones:
        if p['promedio'] > minimo: #p diccionario con las puntuaciones
            filtrados = filtrados + [p]
    return filtrados

def promedios_jurados(puntuaciones):
    """
    Calcula el promedio de puntuaciones de cada jurado.
    
    Args:
        puntuaciones (list): Lista de diccionarios con datos de participantes
    
    Returns:
        dict: Promedios por jurado
    """
    suma_jurado1 = suma_jurado2 = suma_jurado3 = 0
    for p in puntuaciones:
        suma_jurado1 += p['jurado1']
        suma_jurado2 += p['jurado2']
        suma_jurado3 += p['jurado3']
    
    total = len(puntuaciones)
    return {
        'Jurado 1': suma_jurado1 / total,
        'Jurado 2': suma_jurado2 / total,
        'Jurado 3': suma_jurado3 / total
    }

def jurado_mas_estricto(promedios_jurados):
    """
    Identifica al/los jurado(s) con el promedio más bajo.
    
    Args:
        promedios_jurados (dict): Promedios por jurado
    
    Returns:
        list: Nombres de los jurados más estrictos
    """
    min_prom = min(promedios_jurados.values())
    return [j for j, prom in promedios_jurados.items() if prom == min_prom]

def buscar_participante(puntuaciones, nombre):
    """
    Busca participante por nombre.
    
    Args:
        puntuaciones (list): Lista de diccionarios con datos de participantes
        nombre (str): Nombre a buscar
    
    Returns:
        dict or None: Datos del participante o None si no se encuentra
    """
    for p in puntuaciones:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None

def top_tres(puntuaciones):
    """
    Da los tres participantes con mayor promedio.
    
    Args:
        puntuaciones (list): Lista de diccionarios con datos de participantes
    
    Returns:
        list: Top 3 participantes
    """
    # Implementación sin usar sort o sorted
    copia = puntuaciones.copy() #copi asi no la modifica ya que sino se pierde la lista original para otros casos
    top = []
    
    for _ in range(3): 
        if not copia: #si no quedan participantes, sale del bucle
            break
        max_p = copia[0]
        for p in copia[1:]: #recorre el resto de participantes
            if p['promedio'] > max_p['promedio']:   #compara promedios
                max_p = p #nuevo máximo encontrado
        top = top + [max_p] #agrega al top
        copia.remove(max_p)
    
    return top

def ordenar_alfabeticamente(puntuaciones):
    """
    Ordena participantes alfabéticamente.
    
    Args:
        puntuaciones (list): Lista de diccionarios con datos de participantes
    
    Returns:
        list: Participantes ordenados
    """
    
    ordenados = puntuaciones.copy()
    n = len(ordenados)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if ordenados[j]['nombre'].lower() > ordenados[j+1]['nombre'].lower(): #compara nombres
                ordenados[j], ordenados[j+1] = ordenados[j+1], ordenados[j] #intercambia si están en orden incorrecto
    # Devuelve la lista ordenada
    
    return ordenados