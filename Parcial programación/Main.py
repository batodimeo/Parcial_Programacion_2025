from Funciones import (
    cargar_participantes,
    cargar_puntuaciones,
    mostrar_puntuaciones,
    filtrar_por_promedio,
    promedios_jurados,
    jurado_mas_estricto,
    buscar_participante,
    top_tres,
    ordenar_alfabeticamente
)
from Inputs import obtener_entero

def mostrar_menu():
    print("-"*45)
    print("              Menu de opciones")
    print("-"*45)
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Participantes con promedio mayor 4")
    print("5. Participantes con promedio mayor 7")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Buscar participante por nombre")
    print("9. Top 3 participantes")
    print("10. Participantes ordenados alfabéticamente")
    print("0. Salir")

def main():
    participantes = []
    puntuaciones = []
    
    while True:
        mostrar_menu()
        opcion = obtener_entero("\nSeleccione una opción: ", 0, 10)
        
        if opcion == 0:
            print("Saliste")
            break
        
        elif opcion == 1:
            participantes = cargar_participantes()
            print("\nParticipantes cargados\n")
            print("\n")
        
        elif opcion == 2:
            if not participantes:
                print("Error: Falta cargar a los participantes")
                continue
            puntuaciones = cargar_puntuaciones(participantes)
            print("\nPuntuaciones cargadas")
            salir_opcion = input("\nPara salir tocar cualquier tecla")
        
        elif opcion == 3:
            if not puntuaciones:
                print("Error: Primero cargar participantes y las puntuaciones")
                continue
            mostrar_puntuaciones(puntuaciones)
            salir_opcion = input("\nPara salir tocar cualquier tecla")
        
        elif opcion == 4:
            if not puntuaciones:
                print("Error: Primero debe cargar participantes y las puntuaciones")
                continue
            filtrados = filtrar_por_promedio(puntuaciones, 4)
            if filtrados:
                print("\nParticipantes con promedio mayor a 4:")
                mostrar_puntuaciones(filtrados)
                salir_opcion = input("\nPara salir tocar cualquier tecla")
            else:
                print("\nNo hay participantes con promedio mayor a 4")
        
        elif opcion == 5:
            if not puntuaciones:
                print("Error: Primero debe cargar participantes y las puntuaciones")
                continue
            filtrados = filtrar_por_promedio(puntuaciones, 7)
            if filtrados:
                print("\nParticipantes con promedio mayor a 7:")
                mostrar_puntuaciones(filtrados)
                salir_opcion = input("\nPara salir tocar cualquier tecla")
            else:
                print("\nNo hay participantes con promedio mayor a 7")
        
        elif opcion == 6:
            if not puntuaciones:
                print("Error: Primero cargar participantes y las puntuaciones")
                continue
            promedios = promedios_jurados(puntuaciones)
            print("\nPromedios de los jurados:")
            for jurado, prom in promedios.items(): #Promedios diccionario con jurados como claves y sus promedios como valores
                print(f"  {jurado}: {prom:.2f}") #2f para mostrar dos decimales
            salir_opcion = input("\nPara salir tocar cualquier tecla")
        
        elif opcion == 7:
            if not puntuaciones:
                print("Error: Primero cargar participantes y las puntuaciones") 
                continue
            promedios = promedios_jurados(puntuaciones)
            estrictos = jurado_mas_estricto(promedios)
            print("\nJurado más estricto:")
            for j in estrictos:
                print(f"  {j} con promedio {promedios[j]:.2f}")
            salir_opcion = input("\nPara salir tocar cualquier tecla")
        
        elif opcion == 8:
            if not puntuaciones:
                print("Error: Primero cargar participantes y las puntuaciones")
                continue 
            nombre = input("\nIngrese el nombre del participante: ")
            participante = buscar_participante(puntuaciones, nombre)
            if participante:
                print("\nInformacion del participante:")
                mostrar_puntuaciones([participante])
                salir_opcion = input("\nPara salir tocar cualquier tecla")
            else:
                print("\nParticipante no encontrado")
        
        elif opcion == 9:
            if not puntuaciones:
                print("Error: Primero cargar participantes y las puntuaciones")
                continue
            top = top_tres(puntuaciones)
            print("\nTop 3 participantes:")
            mostrar_puntuaciones(top)
            salir_opcion = input("\nPara salir tocar cualquier tecla")
        
        elif opcion == 10:
            if not puntuaciones:
                print("Error: Primero cargar participantes y las puntuaciones")
                continue
            ordenados = ordenar_alfabeticamente(puntuaciones)
            print("\nParticipantes ordenados alfabéticamente:")
            mostrar_puntuaciones(ordenados)
            salir_opcion = input("\nPara salir tocar cualquier tecla")

if __name__ == "__main__": #Forma correcta de ejecutar el main
    main()