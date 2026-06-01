"""Simulacion Monte Carlo para el Problema B: monedas."""

import random


SEMILLA = 2026
NUM_SIMULACIONES = 10000

NUM_MONEDAS = 3
CARA = "cara"
CRUZ = "cruz"
RESULTADOS_MONEDA = (CARA, CRUZ)
NUM_CARAS_OBJETIVO = 2


def lanzar_monedas(numero_monedas):
    """Simula lanzamientos independientes de monedas justas.

    Una moneda justa se modela eligiendo uniformemente entre cara y cruz. La
    independencia se obtiene generando cada moneda por separado.
    """
    return [random.choice(RESULTADOS_MONEDA) for _ in range(numero_monedas)]


def contar_caras(resultados):
    """Cuenta cuantas caras aparecieron en un ensayo.

    Este conteo define la variable aleatoria X del problema: numero de caras en
    el lanzamiento de tres monedas.
    """
    return sum(1 for resultado in resultados if resultado == CARA)


def evento_exactamente_dos_caras(resultados):
    """Evalua el evento de obtener exactamente dos caras."""
    return contar_caras(resultados) == NUM_CARAS_OBJETIVO


def estimar_probabilidad_y_esperanza(num_simulaciones):
    """Estima P(exactamente dos caras) y E[X] usando simulacion.

    La probabilidad se calcula como frecuencia relativa del evento. El valor
    esperado se aproxima con el promedio observado de la variable aleatoria X.
    """
    conteo_exactamente_dos_caras = 0
    suma_valores_x = 0

    for _ in range(num_simulaciones):
        resultados = lanzar_monedas(NUM_MONEDAS)
        numero_caras = contar_caras(resultados)
        suma_valores_x += numero_caras

        if numero_caras == NUM_CARAS_OBJETIVO:
            conteo_exactamente_dos_caras += 1

    probabilidad = conteo_exactamente_dos_caras / num_simulaciones
    esperanza = suma_valores_x / num_simulaciones
    return probabilidad, esperanza


def mostrar_resultados(probabilidad_dos_caras, esperanza_x):
    """Imprime los resultados con formato uniforme y cuatro decimales."""
    print("=" * 50)
    print("PROBLEMA B - MONEDAS")
    print("=" * 50)
    print()
    print(
        f"P(exactamente {NUM_CARAS_OBJETIVO} caras): "
        f"{probabilidad_dos_caras:.4f}"
    )
    print()
    print(f"E[X], donde X = numero de caras: {esperanza_x:.4f}")
    print()
    print("=" * 50)


def main():
    """Ejecuta la simulacion completa del problema B."""
    random.seed(SEMILLA)
    probabilidad_dos_caras, esperanza_x = estimar_probabilidad_y_esperanza(
        NUM_SIMULACIONES
    )
    mostrar_resultados(probabilidad_dos_caras, esperanza_x)


if __name__ == "__main__":
    main()
