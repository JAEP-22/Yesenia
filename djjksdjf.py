import numpy as np

# Parámetro de la distribución de Poisson (promedio de tacos vendidos)
lambda_ = 100

# Generar 1000 números aleatorios siguiendo una distribución de Poisson
demanda_simulada = np.random.poisson(lam=lambda_, size=1000)

# Analizar los resultados (por ejemplo, calcular la media, desviación estándar, etc.)
print(np.mean(demanda_simulada))
print(np.std(demanda_simulada))