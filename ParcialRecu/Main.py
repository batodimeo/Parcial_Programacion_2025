import Funciones as f

participantes = [["", 0, 0, 0] for _ in range(5)]
cargado = False 
puntajes_cargados = False

while True:
    print("-"*45)
    print("        Menu del concurso de baile")
    print("-"*45)
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio > 4")
    print("5. Participantes con promedio > 7")
    print("6. Promedio por jurado")
    print("7. Jurado más estricto")
    print("8. Buscar participante por nombre")
    print("9. Top 3")
    print("10. Ordenar alfabéticamente")
    print("11. Mostrar ganador.")
    print("12. Desempate entre los dos primeros")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        f.cargar_nombres(participantes)
        cargado = True
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "2":
        if cargado:
            f.cargar_puntajes(participantes)
            puntajes_cargados = True
        else:
            print("\nPrimero debe cargar los nombres.\n")
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "3":
        if puntajes_cargados:
            f.mostrar_participantes(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")
        
    elif opcion == "4":
        if puntajes_cargados:
            f.filtrar_por_promedio(participantes, 4)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "5":
        if puntajes_cargados:
            f.filtrar_por_promedio(participantes, 7)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "6":
        if puntajes_cargados:
            f.calcular_promedio_jurados(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "7":
        if puntajes_cargados:
            f.determinar_jurado_estricto(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "8":
        if puntajes_cargados:
            nombre = input("Ingrese el nombre a buscar: ")
            f.buscar_participante(participantes, nombre)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")

    elif opcion == "9":
        if puntajes_cargados:
            f.calcular_top_3(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")

    elif opcion == "10":
        if puntajes_cargados:
            f.ordenar_participantes_alfabeticamente(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        opcion_salir = input("\nPara salir toque enter")
    
    elif opcion == "11":
        if puntajes_cargados:
            f.mostrar_ganador(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")
        
    elif opcion == "12":
        if puntajes_cargados:
            f.desempate(participantes)
        else:
            print("\nPrimero debe cargar nombres/puntuaciones.\n")

    elif opcion == "0":
        break

    else:
        print("\nOpción no válida o datos no cargados aún.\n")