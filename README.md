# Análisis Climático Histórico

## Integrantes del equipo

- Facundo Vega
- Hugo (Rol abstracto: Líder y Organizador)
- Paco (Rol abstracto: Desarrollador Técnico)
- Luis (Rol abstracto: Revisor y QA)

## Escenario elegido

**Escenario A – Análisis de Datos Climáticos**

Este proyecto corresponde al Trabajo Práctico N.º 2 de Organización Empresarial (UTN), desarrollado bajo metodología de trabajo colaborativo con control de versiones distribuido utilizando Git, GitHub, Google Colab y Jira.

## Descripción del dataset utilizado

El dataset utilizado fue construido mediante integración y procesamiento de datos climáticos históricos provenientes de fuentes públicas internacionales.

### Fuente de precipitaciones globales por país (1940–2025)

Datos obtenidos de Our World in Data:

https://ourworldindata.org/grapher/average-precipitation-per-year

A partir de estos registros se realizó una agregación anual global promedio para su posterior análisis estadístico.

### Fuente de temperaturas mínimas y máximas globales (1850–2025)

Datos obtenidos de Berkeley Earth:

https://berkeleyearth.org/data/

Se utilizaron anomalías térmicas históricas de temperatura mínima y máxima anual, posteriormente filtradas y adaptadas al período 1940–2025 para garantizar consistencia temporal con la serie de precipitaciones.

### Variables finales del dataset procesado

- **year** → año de registro
- **min_temp** → temperatura mínima anual
- **max_temp** → temperatura máxima anual
- **precipitacion** → promedio global anual de precipitaciones

El dataset final consolidado fue almacenado en:

```plaintext
datos/clima_datos.csv
```

## Estructura del proyecto

```plaintext
analisis-climatico/
│
├── datos/
│   └── clima_datos.csv
│
├── scripts/
│   └── analisis.py
│
├── resultados/
│   ├── estadisticas.txt
│   └── grafico_temperatura.png
│
└── README.md
```

## Instrucciones para ejecutar el script

Clonar repositorio:

```bash
git clone https://github.com/VegaFacundo/analisis-climatico.git
```

Ingresar al proyecto:

```bash
cd analisis-climatico
```

El proyecto requiere Python 3.x y las siguientes librerías:

```bash
pip install pandas matplotlib
```

Ejecutar análisis:

```bash
python scripts/analisis.py
```

## Resultados generados

La ejecución genera automáticamente:

- métricas estadísticas básicas
- temperatura promedio histórica
- temperatura máxima y mínima
- promedio global de precipitaciones
- gráfico temporal de evolución térmica

Los resultados se almacenan en la carpeta:

```plaintext
/resultados
```

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Google Colab
- Jira
