# Análisis Distribuido de Logs Web con Hadoop MapReduce

Proyecto de **Computación Distribuida y Paralela** (7.º Semestre - Ingeniería de Software).  
Implementación del paradigma **MapReduce** utilizando **Python** y **Hadoop Streaming** para analizar registros de tráfico de un servidor web y contabilizar respuestas HTTP (`200`, `404`, `500`, `403`).

## Estructura del Proyecto
- `generar_logs.py`: Genera un dataset simulado (`access.log`) con 50,000 registros de tráfico web.
- `mapper.py`: Fase **Map**. Extrae el código de estado HTTP de cada línea del log y emite pares `(Código, 1)`.
- `reducer.py`: Fase **Reduce**. Agrupa los códigos ordenados y calcula el total de peticiones por estado.
- `docker-compose.yml`: Configuración opcional para desplegar un entorno Hadoop en contenedores.

## Prueba rápida en Consola (Windows / Linux)
Para verificar la lógica MapReduce localmente antes de subirlo al clúster HDFS:

1. Generar los datos de prueba:
   ```bash
   python generar_logs.py

Bash
type access.log | python mapper.py | sort | python reducer.py

---

### Cómo probarlo en Windows
1. 
   ```powershell
   python generar_logs.py
   type access.log | python mapper.py | sort | python reducer.py
