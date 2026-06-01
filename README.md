# Parcial 4 - Teoría de Probabilidades (MM3014)

Simulaciones Monte Carlo desarrolladas para el Parcial 4 del curso **MM3014 - Teoría de Probabilidades**.

## Autores

- Emily Góngora
- Alejandro Pérez

---

## Descripción

Este proyecto contiene la implementación de cuatro experimentos probabilísticos utilizando simulación Monte Carlo.

Cada programa realiza exactamente **10,000 simulaciones**, utiliza una **semilla fija (2026)** para garantizar reproducibilidad y presenta los resultados con **cuatro decimales**.

La estructura fue diseñada para facilitar modificaciones futuras durante la segunda parte del parcial, donde podrían cambiarse condiciones, eventos o parámetros de los experimentos.

---

## Estructura del proyecto

```text
.
├── problema_a_dados.py
├── problema_b_monedas.py
├── problema_c_canicas.py
├── problema_d_cartas.py
└── README.md
```

---

## Problema A - Dados

Simulación del lanzamiento de dos dados justos de seis caras.

### Se estima:

- \( P(\text{suma} = 7) \)
- \( P(\text{suma} = 7 \mid \text{al menos un dado es par}) \)

---

## Problema B - Monedas

Simulación del lanzamiento de tres monedas justas.

### Se estima:

- \( P(\text{exactamente 2 caras}) \)
- \( E[X] \), donde \( X \) es el número de caras obtenidas

---

## Problema C - Canicas

### Parte 1

Caja con:

- 5 rojas
- 3 azules
- 2 verdes

Se extraen dos canicas sin reemplazo.

Se estima:

- \( P(\text{ambas rojas}) \)

### Parte 2

Dos cajas con diferentes composiciones de colores.

Se selecciona una caja al azar y se extraen dos canicas sin reemplazo.

Dado que se observa una canica roja y una verde, se estima:

- \( P(\text{Caja 1} \mid \text{una roja y una verde}) \)

---

## Problema D - Cartas

Simulación de extracción de cartas de una baraja estándar de 52 cartas sin reemplazo.

### Se estima:

- \( P(\text{ambas son ases}) \)

Además se analizan los eventos:

- \( A \): la primera carta es un as
- \( B \): la segunda carta es un as

Calculando:

- \( P(A) \)
- \( P(B) \)
- \( P(A \cap B) \)
- \( P(A)P(B) \)

para determinar si los eventos son independientes.

---

## Requisitos

- Python 3.x
- Librerías estándar de Python únicamente

No se requieren dependencias externas.

---

## Ejecución

Ejecutar cada archivo de forma independiente:

```bash
python problema_a_dados.py
```

```bash
python problema_b_monedas.py
```

```bash
python problema_c_canicas.py
```

```bash
python problema_d_cartas.py
```

---

## Características de implementación

- Semilla fija para reproducibilidad (`2026`).
- Exactamente `10,000` simulaciones por experimento.
- Código modular y documentado.
- Comentarios explicativos en español.
- Parámetros configurables para facilitar modificaciones futuras.
- Separación entre simulación, cálculo y presentación de resultados.

---

## Notas

Las respuestas se obtienen mediante simulación Monte Carlo y pueden variar ligeramente respecto a los valores teóricos esperados debido al carácter aleatorio del método.

Todos los resultados se muestran con cuatro decimales.
