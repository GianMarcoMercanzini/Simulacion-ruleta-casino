import argparse
import numpy as np
import matplotlib.pyplot as plt

def parsear_argumentos():
    #Parsea los argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description='Simulación de Ruleta - TP 1.1',
        epilog='Ejemplo: python programa.py -t 100 -c 1000 -e 17'
    )
    
    parser.add_argument('-t', '--tiradas', 
                        type=int, 
                        required=True,
                        help='Cantidad de tiradas por corrida')
    
    parser.add_argument('-c', '--corridas', 
                        type=int, 
                        required=True,
                        help='Cantidad de corridas')
    
    parser.add_argument('-e', '--elegido', 
                        type=int, 
                        required=True,
                        help='Número elegido (0-36)')
    
    return parser.parse_args()

def iniciarValoresRuleta():
    # Intentar obtener valores de argumentos de línea de comandos
    try:
        args = parsear_argumentos()
        cantidadTiradas = args.tiradas
        cantidadCorridas = args.corridas
        numeroElegido = args.elegido
        
        # Validaciones
        while cantidadTiradas <= 0:
            print("\n[ERROR] La cantidad de tiradas debe ser un número positivo. Por favor, intente nuevamente.")
            cantidadTiradas = int(input("Ingrese la cantidad de tiradas: "))
            
        while cantidadCorridas <= 0:
            print("\n[ERROR] La cantidad de corridas debe ser un número positivo. Por favor, intente nuevamente.")
            cantidadCorridas = int(input("Ingrese la cantidad de corridas: "))
        
        while not (0 <= numeroElegido <= 36):
            print("\n[ERROR] El número elegido debe estar entre 0 y 36. Por favor, intente nuevamente.")
            numeroElegido = int(input("Ingrese el número elegido (0-36): "))
            
    except SystemExit:
        # Si no se proporcionan argumentos o hay error, usar entrada por consola
        print("\nNo se ingresaron argumentos. Ingresalos a mano:\n")
        
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
    return mediaAritmetica

mediaAritmetica = calcularMediaAritmetica(valores)

# Calculo de la frecuencia relativa del numero elegido
def calcularFrecuenciaRelativa(valores, numeroElegido):

    frecuenciaRelativa = np.sum(valores == numeroElegido) / (cantidadCorridas * cantidadTiradas)
    print("Frecuencia relativa del nro elegido: ", frecuenciaRelativa)

calcularFrecuenciaRelativa(valores, numeroElegido)

# Valor de la varianza y desvio estandar
def calcularVarianzaYDesvioEstandar(valores):

    varianza = np.var(valores)
    print("Varianza: ",varianza)
    desvioEstandar = np.sqrt(varianza)
    print("Desvio Estandar:", desvioEstandar)
    return desvioEstandar

desvioEstandar = calcularVarianzaYDesvioEstandar(valores)

# Graficar dispersion de los valores obtenidos, media aritmetica y desvio estandar
def graficarDesvioEstandar(valores):
    datos = valores.flatten()
    media = np.mean(datos)
    desvio = np.std(datos)
    
    plt.figure(figsize=(12, 5))
    plt.scatter(range(len(datos)), datos, alpha=0.3, s=5, color='blue')
    plt.axhline(media, color='red', linewidth=2, label=f'Media = {media:.2f}')
    plt.axhline(media + desvio, color='orange', linestyle='--', alpha=0.7)
    plt.axhline(media - desvio, color='orange', linestyle='--', alpha=0.7)
    plt.fill_between(range(len(datos)), media - desvio, media + desvio, alpha=0.2)
    plt.title(f'Desvío Estándar = {desvio:.2f}')
    plt.legend()
    plt.show()


# Graficar Histograma Frecuencia relativa de cada nro y destacar el nro elegido
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
graficarDesvioEstandar(valores)

# Graficar Frecuencia Relativa,Varianza Acumulada 
def graficasacumuladas(valores, numeroElegido):

    # Frecuencia Relativa Acumulada
    todos = valores.flatten()
    frecuenciaAcumulada = np.cumsum(todos == numeroElegido) / np.arange(1, len(todos)+1)
    plt.plot(frecuenciaAcumulada)
    plt.xlabel("Número de tiradas (n)")
    plt.ylabel("Frecuencia Relativa")
    plt.axhline(y=1/37, color='red', label='Frecuencia esperada (1/37)')
    plt.title(f'Frecuencia Relativa Acumulada del número {numeroElegido} (línea roja = 1/37)')
    plt.show()

    # Varianza
    varz = [np.var(todos[:i]) for i in range(1, len(todos)+1)]
    plt.plot(varz)
    plt.xlabel("Número de tiradas (n)")
    plt.ylabel("Varianza")
    plt.axhline(y=np.var(np.arange(37)), color='red',  label='Varianza esperada')
    plt.title('Varianza (línea roja = varianza teórica de 0 a 36)')
    plt.show()

    # Desvio Estandar
    desvi = [np.std(todos[:i]) for i in range(1, len(todos)+1)]
    plt.plot(desvi)
    plt.xlabel("Número de tiradas (n)")
    plt.ylabel("Desvío Estándar")
    plt.axhline(y=np.std(np.arange(37)), color='red',label='Desvío esperado' )
    plt.title('Desvío Estándar (línea roja = desvío teórico de 0 a 36)')
    plt.show()

    # Promedio
    prom = np.cumsum(todos) / np.arange(1, len(todos)+1)
    plt.plot(prom ,label='Promedio')
    plt.xlabel("Número de tiradas (n)")
    plt.ylabel("Promedio")
    plt.axhline(y=np.mean(np.arange(37)), color='red',label='Media esperada (18)' )
    plt.title('Promedios')
    plt.show()

graficasacumuladas(valores, numeroElegido)