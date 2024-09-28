import random

def obtener_eleccion_computadora():
    return random.choice(['piedra', 'papel', 'tijeras'])

def obtener_ganador(eleccion_jugador, eleccion_computadora):
    if eleccion_jugador == eleccion_computadora:
        return 'empate'
    elif (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_jugador == 'tijeras' and eleccion_computadora == 'papel'):
        return 'ganar'
    else:
        return 'perder'

def main():
    puntaje = {'ganar': 0, 'perder': 0, 'empate': 0}
    while True:
        eleccion_jugador = input("Ingresa piedra, papel o tijeras (o 'salir' para dejar de jugar): ").lower()
        if eleccion_jugador == 'salir':
            break
        if eleccion_jugador not in ['piedra', 'papel', 'tijeras']:
            print("Entrada inválida. Por favor, intenta de nuevo.")
            continue

        eleccion_computadora = obtener_eleccion_computadora()
        print(f"La computadora eligió: {eleccion_computadora}")

        resultado = obtener_ganador(eleccion_jugador, eleccion_computadora)
        puntaje[resultado] += 1

        if resultado == 'ganar':
            print("¡Ganaste!")
        elif resultado == 'perder':
            print("¡Perdiste!")
        else:
            print("¡Es un empate!")

    print(f"Puntaje final - Ganadas: {puntaje['ganar']}, Perdidas: {puntaje['perder']}, Empates: {puntaje['empate']}")

if __name__ == "__main__":
    main()