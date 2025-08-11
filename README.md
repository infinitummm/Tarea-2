 Comparación de algoritmos de factorial

Objetivo
Comparar las implementaciones recursiva e iterativa del cálculo de factorial en términos de tiempo y uso de memoria.

Métodos
- Python: Medición con `time` y `memory_profiler`
- C: Medición con `clock()` y análisis con Valgrind

Resultados
Se presenta una gráfica comparando los tiempos de ejecución para diferentes valores de n.

Conclusiones
- La versión iterativa tiende a usar menos pila y evita límite de recursión.
- En Python, para valores grandes, la iterativa suele ser más estable; la recursiva puede alcanzar. 


