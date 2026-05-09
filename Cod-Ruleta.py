import numpy as np
import matplotlib.pyplot as plt

def iniciarValoresRuleta():
    
    cantidadTiradas = int(input("Ingrese la cantidad de tiradas: "))
    while cantidadTiradas <= 0:
        print("\n[ERROR] La cantidad de tiradas debe ser un número positivo. Por favor, intente nuevamente.")
        cantidadTiradas = int(input("Ingrese la cantidad de tiradas: "))
        
    cantidadCorridas = int(input("Ingrese la cantidad de corridas: "))
    while cantidadCorridas <= 0:
        print("\n[ERROR] La cantidad de corridas debe ser un número positivo. Por favor, intente nuevamente.")
        cantidadCorridas = int(input("Ingrese la cantidad de corridas: "))
    
    numeroElegido = int(input("Ingrese el número elegido (0-36): "))
    while not (0 <= numeroElegido <= 36):
        print("\n[ERROR] El número elegido debe estar entre 0 y 36. Por favor, intente nuevamente.")
        numeroElegido = int(input("Ingrese el número elegido (0-36): "))

    return cantidadTiradas, cantidadCorridas, numeroElegido

cantidadTiradas, cantidadCorridas, numeroElegido = iniciarValoresRuleta()

def tiradaRuleta():

    valores = np.random.randint(0, 37, size=(cantidadCorridas, cantidadTiradas))
    print("Valores generados, \n",valores)
    return valores

valores = tiradaRuleta()

# Calculo de la media aritmetica de las tiradas
def calcularMediaAritmetica(valores):
    mediaAritmetica = np.mean(valores)
    print("Media Aritmetica: ", mediaAritmetica)

calcularMediaAritmetica(valores)

# Calculo de la frecuencia relativa del numero elegido
def calcularFrecuenciaRelativa(valores, numeroElegido):

    frecuenciaRelativa = np.sum(valores == numeroElegido) / (cantidadCorridas * cantidadTiradas)
    print("Frecuencia relativa del nro elegido: ", frecuenciaRelativa)

calcularFrecuenciaRelativa(valores, numeroElegido)

def graficarHistograma(valores, numeroElegido):
    # Aplanar el array de valores para contar la frecuencia de cada nro
    todosLosValores = valores.flatten()

    # Calcular la frecuencia relativa de cada nro (0-36)
    frecuenciasRelativas = []
    numeros = np.arange(0, 37)

    for num in numeros:
        freq = np.sum(todosLosValores == num) / len(todosLosValores)
        frecuenciasRelativas.append(freq)

    # Crea la figura
    plt.figure(figsize=(14, 7))

    # Barras del histograma
    barras = plt.bar(numeros, frecuenciasRelativas, width=0.8, color='skyblue', edgecolor='black', alpha=0.7)

    # Resaltar el nro elegido
    barras[numeroElegido].set_color('red')
    barras[numeroElegido].set_alpha(0.8)

    # Línea de frecuencia esperada
    frecuenciaEsperada = 1 / 37
    plt.axhline(y=frecuenciaEsperada, color='green', linestyle='--', linewidth=2, label=f'Frecuencia esperada (1/37) ≈ {frecuenciaEsperada:.4f}')

    # Configuración del gráfico
    plt.xlabel('Números de la ruleta', fontsize=12, fontweight='bold')
    plt.ylabel('Frecuencia relativa', fontsize=12, fontweight='bold')
    plt.title(f'Histograma de frecuencias relativas\nNúmero {numeroElegido} destacado en rojo\n'
            f'{cantidadCorridas} corridas x {cantidadTiradas} tiradas = {len(todosLosValores)} tiradas totales', fontsize=13, fontweight='bold')
    plt.xticks(np.arange(0, 37, step=2))
    plt.yticks(np.arange(0, max(frecuenciasRelativas) + 0.01, 0.01))
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.legend(loc='upper right')

    # Agregar el valor de la frecuencia relativa del nro elegido encima de su barra
    plt.text(numeroElegido, frecuenciasRelativas[numeroElegido] + 0.001, f'{frecuenciasRelativas[numeroElegido]:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

graficarHistograma(valores, numeroElegido)

# Valor de la varianza
# Valor del desvio estandar
