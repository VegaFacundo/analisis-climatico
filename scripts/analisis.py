import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("resultados", exist_ok=True)


df = pd.read_csv("datos/clima_datos.csv")

df["temp_promedio"] = (df["min_temp"] + df["max_temp"]) / 2

temp_promedio_global = df["temp_promedio"].mean()
temp_maxima = df["max_temp"].max()
temp_minima = df["min_temp"].min()
precipitacion_promedio = df["precipitacion"].mean()


with open("resultados/estadisticas.txt", "w") as f:
    f.write(f"Temperatura promedio: {temp_promedio_global:.3f}\n")
    f.write(f"Temperatura máxima: {temp_maxima:.3f}\n")
    f.write(f"Temperatura mínima: {temp_minima:.3f}\n")
    f.write(f"Promedio precipitaciones: {precipitacion_promedio:.3f}\n")


plt.figure(figsize=(15, 6))
plt.plot(df["year"], df["temp_promedio"])

plt.title("Evolución de la Temperatura Promedio en el Tiempo")
plt.xlabel("Año")
plt.ylabel("Temperatura Promedio (°C)")
plt.grid(True)

plt.tight_layout()
plt.savefig("resultados/grafico_temperatura.png")
plt.show()

print("Análisis completado correctamente.")
