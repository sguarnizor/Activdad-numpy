"""Tabla de posiciones de la Champions League con NumPy y Matplotlib."""

import numpy as np
import matplotlib

matplotlib.use("Agg")  # backend sin ventana, para guardar el PNG
import matplotlib.pyplot as plt

ARCHIVO_ENTRADA = "equiposChampions.csv"
ARCHIVO_SALIDA = "tabla_posiciones.csv"
ARCHIVO_GRAFICA = "grafica_puntos.png"

# 1. Lectura con NumPy
# Columnas de texto (equipo, pais) y columnas numericas por separado
textos = np.genfromtxt(
    ARCHIVO_ENTRADA, delimiter=",", skip_header=1,
    usecols=(0, 1), dtype=str, encoding="utf-8",
)
equipos = textos[:, 0]

# Arreglo numerico: ganados, empatados, perdidos, goles_favor, goles_contra
datos = np.genfromtxt(
    ARCHIVO_ENTRADA, delimiter=",", skip_header=1,
    usecols=(2, 3, 4, 5, 6), dtype=int, encoding="utf-8",
)
ganados = datos[:, 0]
empatados = datos[:, 1]
perdidos = datos[:, 2]
goles_favor = datos[:, 3]
goles_contra = datos[:, 4]

# 2. Puntos: 3 por victoria, 1 por empate, 0 por derrota
puntos = ganados * 3 + empatados * 1 + perdidos * 0

# 3. Diferencia de goles
diferencia_goles = goles_favor - goles_contra

# 4. Guardar resultados en tabla_posiciones.csv
with open(ARCHIVO_SALIDA, "w", encoding="utf-8", newline="") as f:
    f.write("equipo,puntos,diferencia_goles\n")
    for equipo, pts, dg in zip(equipos, puntos, diferencia_goles):
        f.write(f"{equipo},{pts},{dg}\n")

# 5. Grafica de barras (ordenada de mayor a menor puntaje)
orden = np.argsort(-puntos, kind="stable")
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(equipos[orden], puntos[orden], color="#1f4e9c")
ax.set_title("Puntos obtenidos por equipo - Champions League")
ax.set_xlabel("Equipo")
ax.set_ylabel("Puntos")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
fig.tight_layout()
fig.savefig(ARCHIVO_GRAFICA, dpi=150)

print(f"Equipos procesados: {len(equipos)}")
print(f"Archivos generados: {ARCHIVO_SALIDA}, {ARCHIVO_GRAFICA}")