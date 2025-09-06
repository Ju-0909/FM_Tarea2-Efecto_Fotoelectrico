"""
created on Fri Aug 29 00:56:12 2025
@author: Jk9
"""

# ------------------------------------------
# Análisis de datos fotoeléctricos en Python
# ------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
frecuencia = np.array([5.00e14, 5.50e14, 6.00e14, 6.50e14, 7.00e14, 7.50e14, 8.00e14])  # Frecuencia v - Hz
V0 = np.array([0.20, 0.45, 0.70, 0.92, 1.18, 1.42, 1.68])  # Vo (V)

# Parte (a) - Gráfica de V0 vs frecuencia
plt.figure(figsize=(8,6))
plt.plot(frecuencia, V0, 'o', label='Datos experimentales')
plt.xlabel('Frecuencia ν (Hz)')
plt.ylabel('Potencial de detención V₀ (V)')
plt.title('Potencial de detención V₀ vs Frecuencia ν')
plt.grid(False)
plt.legend()
plt.show()

# Parte (b) - Ajuste lineal
coef = np.polyfit(frecuencia, V0, 1)  # coef[0] = pendiente, coef[1] = intercepto
m, b = coef

# Mostrar resultados del ajuste
print(f"Pendiente (m = h/e): {m:.3e} V·s")
print(f"Ordenada al origen (b = -φ/e): {b:.3f} V")

# Graficar datos y línea ajustada
plt.figure(figsize=(8,6))
plt.plot(frecuencia, V0, 'o', label='Datos experimentales')
plt.plot(frecuencia, m * frecuencia + b, '-', label='Ajuste lineal')
plt.xlabel('Frecuencia ν (Hz)')
plt.ylabel('Potencial de detención V₀ (V)')
plt.title('Ajuste lineal de V₀ vs ν')
plt.grid(False)
plt.legend()
plt.show()

# Parte (c) - Calcular h experimental
e = 1.602e-19  # Carga del electrón en C
h_exp = m * e  # h = m * e
print(f"Constante de Planck experimental: h = {h_exp:.3e} J·s")

# Parte (d) - Calcular función de trabajo φ (en eV)
phi_eV = -b  # φ = -b * e, pero en eV, φ = -b directamente
print(f"Función de trabajo del material: φ = {phi_eV:.3f} eV")
