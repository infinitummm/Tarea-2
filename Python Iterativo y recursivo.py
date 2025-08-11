import time
from memory_profiler import memory_usage

def facto_r(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto_r(n - 1)

def facto_i(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def main():
    n = int(input("Ingresa el valor de n para calcular factorial: "))


    start_time = time.time()
    mem_usage_rec = memory_usage((facto_r, (n,)), interval=0.01)
    resultado_rec = facto_r(n)
    end_time = time.time()

    print(f"\nRecursiva: Factorial de {n} es {resultado_rec}")
    print(f"Tiempo: {end_time - start_time:.6f} segundos")
    print(f"Memoria usada (recursiva): {max(mem_usage_rec) - min(mem_usage_rec):.6f} MiB")


    start_time = time.time()
    mem_usage_iter = memory_usage((facto_i, (n,)), interval=0.01)
    resultado_iter = facto_i(n)
    end_time = time.time()

    print(f"\nIterativa: Factorial de {n} es {resultado_iter}")
    print(f"Tiempo: {end_time - start_time:.6f} segundos")
    print(f"Memoria usada (iterativa): {max(mem_usage_iter) - min(mem_usage_iter):.6f} MiB")

if __name__ == "__main__":
    main()
