import random
import time

# Función para generar números aleatorios
def generar_numeros_aleatorios(min_val, max_val):
    return random.randint(min_val, max_val)

# Función para realizar una operación (resta, suma, multiplicación, división)
def ejecutar_operacion(operacion, tiempo_limite):
    inicio_tiempo = time.time()
    print(f"Iniciando operación de {operacion} durante {tiempo_limite} segundos.")
    while time.time() - inicio_tiempo < tiempo_limite:
        num1 = generar_numeros_aleatorios(1, 100)
        num2 = generar_numeros_aleatorios(1, 100)
        resultado = None  # Inicializamos resultado con None

        if operacion == "resta":
            resultado = num1 - num2
        elif operacion == "suma":
            resultado = num1 + num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            resultado = num1 / num2

        print(f"Números utilizados para {operacion}: {num1} y {num2}")
        # Verificar si resultado no es None antes de imprimir
        if resultado is not None:
            print(f"Resultado de {operacion}: {resultado}")

# Define el rango de tiempo para cada operación
min_tiempo = 5  # Tiempo mínimo en segundos
max_tiempo = 15  # Tiempo máximo en segundos

# Realiza las operaciones en el orden deseado con tiempos aleatorios
ejecutar_operacion("resta", random.uniform(min_tiempo, max_tiempo))
ejecutar_operacion("suma", random.uniform(min_tiempo, max_tiempo))
ejecutar_operacion("division", random.uniform(min_tiempo, max_tiempo))
ejecutar_operacion("multiplicacion", random.uniform(min_tiempo, max_tiempo))

# Operaciones adicionales
ejecutar_operacion("division", random.uniform(min_tiempo, max_tiempo))
ejecutar_operacion("suma", random.uniform(min_tiempo, max_tiempo))
ejecutar_operacion("resta", random.uniform(min_tiempo, max_tiempo))
