"""Simulacion Monte Carlo para el Problema A: dados."""

import random


SEMILLA = 2026
NUM_SIMULACIONES = 10000

NUM_DADOS = 2
CARAS_DADO = 6
SUMA_OBJETIVO = 7


def lanzar_dados(numero_dados, caras_dado):
    """Simula el lanzamiento de dados justos e independientes."""
    return [random.randint(1, caras_dado) for _ in range(numero_dados)]


def suma_es_objetivo(resultados, suma_objetivo):
    """Indica si la suma de los dados coincide con el valor buscado."""
    return sum(resultados) == suma_objetivo


def al_menos_un_dado_es_par(resultados):
    """Evalua la condicion usada en la probabilidad condicional.

    La condicion no cambia la forma de simular; solo filtra los ensayos que
    pertenecen al espacio muestral condicionado.
    """
    return any(resultado % 2 == 0 for resultado in resultados)


def estimar_probabilidades(num_simulaciones):
    """Estima las probabilidades solicitadas con una sola corrida Monte Carlo.

    Se realizan exactamente num_simulaciones lanzamientos del experimento
    base. Con esos mismos ensayos se calcula la probabilidad simple y la
    condicional, evitando duplicar simulaciones del mismo experimento.
    """
    conteo_suma_objetivo = 0
    conteo_condicion = 0
    conteo_suma_objetivo_y_condicion = 0

    for _ in range(num_simulaciones):
        resultados = lanzar_dados(NUM_DADOS, CARAS_DADO)

        if suma_es_objetivo(resultados, SUMA_OBJETIVO):
            conteo_suma_objetivo += 1

        if al_menos_un_dado_es_par(resultados):
            conteo_condicion += 1
            if suma_es_objetivo(resultados, SUMA_OBJETIVO):
                conteo_suma_objetivo_y_condicion += 1

    probabilidad_simple = conteo_suma_objetivo / num_simulaciones

    if conteo_condicion == 0:
        probabilidad_condicional = 0.0
    else:
        probabilidad_condicional = conteo_suma_objetivo_y_condicion / conteo_condicion

    return probabilidad_simple, probabilidad_condicional


def mostrar_resultados(probabilidad_suma, probabilidad_condicional):
    """Imprime los resultados con formato uniforme y cuatro decimales."""
    print("=" * 50)
    print("PROBLEMA A - DADOS")
    print("=" * 50)
    print()
    print(f"P(suma = {SUMA_OBJETIVO}): {probabilidad_suma:.4f}")
    print()
    print(
        "P(suma = "
        f"{SUMA_OBJETIVO} | al menos un dado es par): "
        f"{probabilidad_condicional:.4f}"
    )
    print()
    print("=" * 50)


def main():
    """Ejecuta la simulacion completa del problema A."""
    random.seed(SEMILLA)
    probabilidad_suma, probabilidad_condicional = estimar_probabilidades(
        NUM_SIMULACIONES
    )
    mostrar_resultados(probabilidad_suma, probabilidad_condicional)


if __name__ == "__main__":
    main()
