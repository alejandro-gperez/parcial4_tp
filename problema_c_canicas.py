"""Simulacion Monte Carlo para el Problema C: canicas."""

import random


SEMILLA = 2026
NUM_SIMULACIONES = 10000

ROJA = "roja"
AZUL = "azul"
VERDE = "verde"

NUM_EXTRACCIONES = 2

CAJA_PARTE_1 = {
    ROJA: 5,
    AZUL: 3,
    VERDE: 2,
}

CAJAS_PARTE_2 = {
    "Caja 1": {
        ROJA: 5,
        AZUL: 3,
        VERDE: 2,
    },
    "Caja 2": {
        ROJA: 2,
        AZUL: 5,
        VERDE: 3,
    },
}

CAJA_OBJETIVO = "Caja 1"


def construir_lista_canicas(configuracion_caja):
    """Convierte una caja descrita por conteos en una lista de canicas.
    """
    canicas = []

    for color, cantidad in configuracion_caja.items():
        canicas.extend([color] * cantidad)

    return canicas


def extraer_sin_reemplazo(configuracion_caja, numero_extracciones):
    """Simula extracciones sin reemplazo desde una caja.

    Sin reemplazo significa que una canica no puede aparecer dos veces en el
    mismo ensayo. random.sample implementa precisamente esa logica.
    """
    canicas = construir_lista_canicas(configuracion_caja)
    return random.sample(canicas, numero_extracciones)


def ambas_son_rojas(canicas_extraidas):
    """Evalua el evento de que las dos canicas extraidas sean rojas."""
    return all(canica == ROJA for canica in canicas_extraidas)


def hay_una_roja_y_una_verde(canicas_extraidas):
    """Evalua el resultado observado: una roja y una verde, sin importar orden."""
    return (
        len(canicas_extraidas) == 2
        and canicas_extraidas.count(ROJA) == 1
        and canicas_extraidas.count(VERDE) == 1
    )


def elegir_caja_al_azar(cajas):
    """Elige una caja con probabilidad uniforme entre las cajas disponibles."""
    nombre_caja = random.choice(list(cajas.keys()))
    return nombre_caja, cajas[nombre_caja]


def estimar_probabilidad_ambas_rojas(num_simulaciones):
    """Estima P(ambas rojas) para una sola caja por frecuencia relativa."""
    conteo_ambas_rojas = 0

    for _ in range(num_simulaciones):
        extraccion = extraer_sin_reemplazo(CAJA_PARTE_1, NUM_EXTRACCIONES)
        if ambas_son_rojas(extraccion):
            conteo_ambas_rojas += 1

    return conteo_ambas_rojas / num_simulaciones


def estimar_probabilidad_caja_dado_resultado(num_simulaciones):
    """Estima P(Caja 1 | una roja y una verde) mediante simulacion.

    Esta es una inferencia tipo Bayes resuelta por conteo Monte Carlo:
    primero se filtran los ensayos donde se observa una roja y una verde; entre
    esos ensayos se calcula que proporcion provino de la caja objetivo.

    Referencia teorica de validacion: el valor correcto es 5/8 = 0.625.
    """
    conteo_resultado_observado = 0
    conteo_caja_objetivo_y_resultado = 0

    for _ in range(num_simulaciones):
        nombre_caja, configuracion_caja = elegir_caja_al_azar(CAJAS_PARTE_2)
        extraccion = extraer_sin_reemplazo(configuracion_caja, NUM_EXTRACCIONES)

        if hay_una_roja_y_una_verde(extraccion):
            conteo_resultado_observado += 1
            if nombre_caja == CAJA_OBJETIVO:
                conteo_caja_objetivo_y_resultado += 1

    if conteo_resultado_observado == 0:
        return 0.0

    return conteo_caja_objetivo_y_resultado / conteo_resultado_observado


def mostrar_resultados(probabilidad_ambas_rojas, probabilidad_caja_1):
    """Imprime los resultados con formato uniforme y cuatro decimales."""
    print("=" * 50)
    print("PROBLEMA C - CANICAS")
    print("=" * 50)
    print()
    print(f"P(ambas rojas): {probabilidad_ambas_rojas:.4f}")
    print()
    print(f"P(Caja 1 | una roja y una verde): {probabilidad_caja_1:.4f}")
    print()
    print("=" * 50)


def main():
    """Ejecuta la simulacion completa del problema C."""
    random.seed(SEMILLA)
    probabilidad_ambas_rojas = estimar_probabilidad_ambas_rojas(NUM_SIMULACIONES)
    probabilidad_caja_1 = estimar_probabilidad_caja_dado_resultado(
        NUM_SIMULACIONES
    )
    mostrar_resultados(probabilidad_ambas_rojas, probabilidad_caja_1)


if __name__ == "__main__":
    main()
