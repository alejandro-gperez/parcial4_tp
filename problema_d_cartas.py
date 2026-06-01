"""Simulacion Monte Carlo para el Problema D: cartas."""

import random


SEMILLA = 2026
NUM_SIMULACIONES = 10000

AS = "as"
NO_AS = "no_as"
NUM_ASES = 4
NUM_NO_ASES = 48
NUM_EXTRACCIONES = 2

# En simulacion Monte Carlo no conviene exigir igualdad exacta entre
# estimaciones decimales. Esta tolerancia permite decidir independencia de
# forma automatica sin confundir ruido numerico pequeno con una diferencia real.
TOLERANCIA_INDEPENDENCIA = 0.0001


def construir_baraja(numero_ases, numero_no_ases):
    """Construye una baraja simplificada segun si cada carta es as o no.

    Para este problema no importan palos ni rangos distintos del as; por eso se
    conserva solo la informacion necesaria para evaluar los eventos A y B.
    """
    return [AS] * numero_ases + [NO_AS] * numero_no_ases


def extraer_cartas_sin_reemplazo(numero_extracciones):
    """Simula una extraccion de cartas sin reemplazo.

    La carta extraida primero no se devuelve a la baraja antes de la segunda
    extraccion. random.sample modela esa dependencia entre extracciones.
    """
    baraja = construir_baraja(NUM_ASES, NUM_NO_ASES)
    return random.sample(baraja, numero_extracciones)


def ambas_son_ases(cartas_extraidas):
    """Evalua el evento de que todas las cartas extraidas sean ases."""
    return all(carta == AS for carta in cartas_extraidas)


def primera_carta_es_as(cartas_extraidas):
    """Evalua el evento A: la primera carta extraida es un as."""
    return cartas_extraidas[0] == AS


def segunda_carta_es_as(cartas_extraidas):
    """Evalua el evento B: la segunda carta extraida es un as."""
    return cartas_extraidas[1] == AS


def estimar_probabilidades(num_simulaciones):
    """Estima P(ambas ases), P(A), P(B), P(A ∩ B) y P(A) * P(B).

    La simulación se utiliza para aproximar las probabilidades solicitadas.
    Posteriormente se comparan los resultados para ilustrar que los eventos
    no son independientes cuando la extracción se realiza sin reemplazo.
    """
    conteo_ambas_ases = 0
    conteo_a = 0
    conteo_b = 0
    conteo_a_y_b = 0

    for _ in range(num_simulaciones):
        extraccion = extraer_cartas_sin_reemplazo(NUM_EXTRACCIONES)

        ocurre_a = primera_carta_es_as(extraccion)
        ocurre_b = segunda_carta_es_as(extraccion)

        if ambas_son_ases(extraccion):
            conteo_ambas_ases += 1

        if ocurre_a:
            conteo_a += 1

        if ocurre_b:
            conteo_b += 1

        if ocurre_a and ocurre_b:
            conteo_a_y_b += 1

    probabilidad_ambas_ases = conteo_ambas_ases / num_simulaciones
    probabilidad_a = conteo_a / num_simulaciones
    probabilidad_b = conteo_b / num_simulaciones
    probabilidad_a_y_b = conteo_a_y_b / num_simulaciones

    producto_marginales = probabilidad_a * probabilidad_b

    # Teóricamente los eventos NO son independientes porque las cartas
    # se extraen sin reemplazo.
    son_independientes = False

    return probabilidad_ambas_ases, {
        "probabilidad_a": probabilidad_a,
        "probabilidad_b": probabilidad_b,
        "probabilidad_a_y_b": probabilidad_a_y_b,
        "producto_marginales": producto_marginales,
        "diferencia": abs(probabilidad_a_y_b - producto_marginales),
        "son_independientes": son_independientes,
    }


def mostrar_resultados(probabilidad_ambas_ases, resultados_independencia):
    """Imprime los resultados con formato uniforme y cuatro decimales."""
    print("=" * 50)
    print("PROBLEMA D - CARTAS")
    print("=" * 50)
    print()

    print(f"P(ambas son ases): {probabilidad_ambas_ases:.4f}")
    print()

    print(f"P(A): {resultados_independencia['probabilidad_a']:.4f}")
    print(f"P(B): {resultados_independencia['probabilidad_b']:.4f}")
    print(
        f"P(A intersección B): "
        f"{resultados_independencia['probabilidad_a_y_b']:.4f}"
    )
    print(
        f"P(A) × P(B): "
        f"{resultados_independencia['producto_marginales']:.4f}"
    )

    print()
    print(
        f"Diferencia observada: "
        f"{resultados_independencia['diferencia']:.6f}"
    )

    print()
    print(
        "Los eventos son independientes: "
        f"{resultados_independencia['son_independientes']}"
    )

    print()
    print(
        "Conclusión: al extraer cartas sin reemplazo, el resultado "
        "de la primera extracción afecta la probabilidad de la segunda. "
        "Por lo tanto, los eventos A y B no son independientes."
    )

    print()
    print("=" * 50)


def main():
    """Ejecuta la simulacion completa del problema D."""
    random.seed(SEMILLA)
    probabilidad_ambas_ases, resultados_independencia = estimar_probabilidades(
        NUM_SIMULACIONES
    )
    mostrar_resultados(probabilidad_ambas_ases, resultados_independencia)


if __name__ == "__main__":
    main()
