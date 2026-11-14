#!/usr/bin/env python3
import sys

for linea in sys.stdin:
  linea = linea.strip()
  if not linea:
    continue

  partes = linea.split()
  # En el formato estándar de log, el código HTTP está en la penúltima posición
  if len(partes) >= 9:
    codigo_http = partes[-2]
    # Emitimos par clave-valor: Codigo_HTTP [TAB] 1
    print(f"{codigo_http}\t1")
