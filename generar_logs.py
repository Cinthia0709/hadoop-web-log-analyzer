import random
from datetime import datetime, timedelta

ips = [
    "192.168.1.10",
    "192.168.1.25",
    "10.0.0.5",
    "172.16.0.12",
    "200.48.10.4",
    "190.235.12.88",
]
rutas = [
    "/index.html",
    "/productos",
    "/login",
    "/carrito",
    "/api/v1/usuarios",
    "/contacto",
]
codigos = [
    200,
    200,
    200,
    200,
    404,
    500,
    403,
]  # Mayor probabilidad de 200 (OK)


def generar_archivo_logs(nombre_archivo="access.log", num_lineas=50000):
  fecha_base = datetime(2026, 11, 10, 8, 0, 0)
  with open(nombre_archivo, "w", encoding="utf-8") as f:
    for i in range(num_lineas):
      ip = random.choice(ips)
      fecha = (fecha_base + timedelta(seconds=i * 2)).strftime(
          "%d/%b/%Y:%H:%M:%S"
      )
      ruta = random.choice(rutas)
      codigo = random.choice(codigos)
      linea = f'{ip} - - [{fecha} -0500] "GET {ruta} HTTP/1.1" {codigo} 1024\n'
      f.write(linea)
  print(f"Archivo '{nombre_archivo}' generado con {num_lineas} registros.")


if __name__ == "__main__":
  generar_archivo_logs()
