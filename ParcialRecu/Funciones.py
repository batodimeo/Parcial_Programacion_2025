import Inputs
import random

def cargar_nombres(participantes):
    """
    Carga los nombres de los 5 participantes en la matriz.
    
    Args:
        participantes: Matriz de participantes donde se almacenarán los nombres en la primera columna
    """
    for i in range(5):
        participantes[i][0] = Inputs.ingresar_nombre()

def cargar_puntajes(participantes):
    """
    Carga los puntajes de los 3 jurados para cada participante.
    
    Args:
        participantes: Matriz de participantes donde se almacenarán los puntajes
    """
    for i in range(5):
        for j in range(3):
            participantes[i][j + 1] = Inputs.ingresar_puntaje(j, participantes[i][0])

def mostrar_participantes(participantes):
    """
    Muestra la información completa de todos los participantes incluyendo sus puntajes y promedio.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    for i in range(5):
        suma = 0
        for j in range(1, 4):
            suma += participantes[i][j]
        promedio = suma / 3
        print(f"\nNOMBRE PARTICIPANTE: {participantes[i][0]}")
        print(f"JURADO 1: {participantes[i][1]}")
        print(f"JURADO 2: {participantes[i][2]}")
        print(f"JURADO 3: {participantes[i][3]}")
        print(f"PROMEDIO: {promedio:.2f}/10\n")

def filtrar_por_promedio(participantes, umbral):
    """
    Filtra y muestra los participantes que tienen un promedio mayor al umbral especificado.
    
    Args:
        participantes: Matriz con la información de todos los participantes
        umbral: Valor mínimo del promedio para filtrar participantes
    """
    encontrado = False
    for i in range(5):
        suma = 0
        for j in range(1, 4):
            suma += participantes[i][j]
        promedio = suma / 3
        if promedio > umbral: #umbral es el valor mínimo del promedio
            print(f"\n{participantes[i][0]} - Promedio: {promedio:.2f}")
            encontrado = True
    if not encontrado:
        print(f"No hay participantes con promedio mayor a {umbral}.")

def calcular_promedio_jurados(participantes):
    """
    Calcula y muestra el promedio de puntajes otorgados por cada jurado.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    for j in range(3):
        suma = 0
        for i in range(5):
            suma += participantes[i][j + 1]
        print(f"Promedio del Jurado {j + 1}: {suma / 5:.2f}")

def determinar_jurado_estricto(participantes):
    """
    Determina cuál es el jurado más estricto basándose en el promedio más bajo de puntajes otorgados.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    promedios = [0, 0, 0]
    for j in range(3):
        suma = 0
        for i in range(5):
            suma += participantes[i][j + 1]
        promedios[j] = suma / 5

    minimo = promedios[0]
    for p in promedios:
        if p < minimo:
            minimo = p

    print("Jurado más estricto:")
    for j in range(3):
        if promedios[j] == minimo:
            print(f"Jurado {j + 1} con promedio {promedios[j]:.2f}")

def buscar_participante(participantes, nombre_buscado):
    """
    Busca un participante por nombre y muestra su información completa.
    
    Args:
        participantes: Matriz con la información de todos los participantes
        nombre_buscado: Nombre del participante a buscar
    """
    for i in range(5):
        if participantes[i][0].lower() == nombre_buscado.lower():
            suma = 0
            for j in range(1, 4):
                suma += participantes[i][j]
            promedio = suma / 3
            print(f"\nNOMBRE PARTICIPANTE: {participantes[i][0]}")
            print(f"JURADO 1: {participantes[i][1]}")
            print(f"JURADO 2: {participantes[i][2]}")
            print(f"JURADO 3: {participantes[i][3]}")
            print(f"PROMEDIO: {promedio:.2f}/10\n")
            return
    print("Participante no encontrado.")

def calcular_top_3(participantes):
    """
    Calcula y muestra los 3 participantes con mejor promedio en orden descendente.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    promedios = [[0, ""] for _ in range(5)]
    for i in range(5):
        suma = 0
        for j in range(1, 4):
            suma += participantes[i][j]
        promedio = suma / 3
        promedios[i][0] = promedio
        promedios[i][1] = participantes[i][0]

    for i in range(4):
        for j in range(i + 1, 5):
            if promedios[i][0] < promedios[j][0]:
                temp = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = temp

    print("Top 3 participantes:")
    for i in range(3):
        for k in range(5):
            if participantes[k][0] == promedios[i][1]:
                print(f"\nNOMBRE PARTICIPANTE: {participantes[k][0]}")
                print(f"JURADO 1: {participantes[k][1]}")
                print(f"JURADO 2: {participantes[k][2]}")
                print(f"JURADO 3: {participantes[k][3]}")
                print(f"PROMEDIO: {promedios[i][0]:.2f}/10\n")
                break

def ordenar_participantes_alfabeticamente(participantes):
    """
    Ordena los participantes alfabéticamente por nombre y los muestra.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    for i in range(4):
        for j in range(i + 1, 5):
            if participantes[i][0].lower() > participantes[j][0].lower():
                temp = participantes[i]
                participantes[i] = participantes[j]
                participantes[j] = temp
    mostrar_participantes(participantes)
    
def mostrar_ganador(participantes):
    """
    Determina y muestra el ganador o ganadores con el promedio más alto.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    max_promedio = -1
    ganadores = []
    for i in range(5):
        suma = 0
        for j in range(1, 4):
            suma += participantes[i][j]
        promedio = suma / 3
        if promedio > max_promedio: #si el promedio es mayor al máximo encontrado actualiza el máximo
            max_promedio = promedio
            ganadores = [participantes[i][0]]
        elif promedio == max_promedio:
            ganadores += [participantes[i][0]]

    if len(ganadores) == 1:
        print(f"\nGANADOR: {ganadores[0]} con un promedio de {max_promedio:.2f}/10\n")
    else:
        print("\nGANADORES: ", end="")
        for i in range(len(ganadores)):
            if i == len(ganadores) - 1:
                print(f"{ganadores[i]}", end="") #end evita el salto de línea
            else:
                print(f"{ganadores[i]}, ", end="")
        print(f" con un promedio de {max_promedio:.2f}/10\n")

def desempate(participantes):
    """
    Realiza un desempate entre los participantes con el promedio más alto.
    Selecciona aleatoriamente uno en caso de empate.
    
    Args:
        participantes: Matriz con la información de todos los participantes
    """
    max_promedio = -1
    ganadores = []
    
    for i in range(5):
        suma = 0
        for j in range(1, 4):
            suma += participantes[i][j]
        promedio = suma / 3
        if promedio > max_promedio:
            max_promedio = promedio
            ganadores = [participantes[i][0]]
        elif promedio == max_promedio:
            ganadores += [participantes[i][0]]
    
    if len(ganadores) > 1:
        elegido = random.choice(ganadores)
        print(f"Desempate realizado entre los ganadores empatados.")
        print(f"El ganador final es: {elegido}")
    else:
        print("No hay empate para desempatar. Solo hay un ganador.")