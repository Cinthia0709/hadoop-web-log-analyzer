#!/usr/bin/env python3
import sys

codigo_actual = None
conteo_actual = 0

for linea in sys.stdin:
  linea = linea.strip()
  if not linea:
    continue

  try:
    codigo, conteo = linea.split("\t", 1)
    conteo = int(conteo)
  except ValueError:
    continue

  if codigo_actual == codigo:
    conteo_actual += conteo
  else:
    if codigo_actual is not None:
      print(f"Codigo HTTP {codigo_actual}:\t{conteo_actual} peticiones")
    codigo_actual = codigo
    conteo_actual = conteo

# Imprimir el último código procesado
if codigo_actual is not None:
  print(f"Codigo HTTP {codigo_actual}:\t{conteo_actual} peticiones")
