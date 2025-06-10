def ingresar_nombre():
    while True:
        nombre = input("Ingrese el nombre del participante: ").strip()
        es_valido = True
        for c in nombre:
            if not (c.isalpha() or c.isspace()):
                es_valido = False
                break
        if len(nombre) >= 3 and es_valido:
            return nombre
        else:
            print("El nombre debe tener al menos 3 letras y solo letras o espacios.")

def ingresar_puntaje(jurado, participante):
    while True:
        try:
            puntaje = int(input(f"Ingrese la puntuación del Jurado {jurado + 1} para {participante}: "))
            if 1 <= puntaje <= 10:
                return puntaje
            else:
                print("Puntaje inválido. Debe estar entre 1 y 10.")
        except ValueError:
            print("Debe ingresar un número entero.")