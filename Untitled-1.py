import numpy as np
import matplotlib.pyplot as plt

def calculo(N, M, v0):
    """
    Funcion principal que crea la matriz y relaja sus valores hasta que no cambian de manera sensible.

    Args:
    - N (int): Puntos de la red en la dimensión x.
    - M (int): Puntos de la red en la dimensión y.
    - v0 (int): Valor inicial del potencial.

    Returns:
    None
    """
    
    matriz=[[0 for i in range(N+2)] for i in range(M+2)]
    for i in range(N+2):
        matriz[0][i]=-v0
        matriz[M+1][i]=v0
    
    max_prov=0
    cent=True

    while cent:
        matriz, max=relaja(matriz)
        if (max-max_prov)<0.0001:
            cent=False
        else:
            max_prov=max

    grafica(matriz)


def relaja(matriz):
    """
    Realiza una relajación de la matriz.

    Args:
    - matriz (list): La matriz a relajar.

    Returns:
    - list: La matriz relajada.
    - float: El valor máximo encontrado en la matriz relajada.
    """
    max=0
    for i in range(1,len(matriz)-1):
        for j in range(1,len(matriz[i])-1):
            matriz[i][j]=(matriz[i-1][j]+matriz[i+1][j]+matriz[i][j-1]+matriz[i][j+1])/4
            if matriz[i][j]>max:
                max=matriz[i][j]
    return matriz, max

def grafica(matriz):
    """
    Genera una gráfica 3D de la matriz.

    Args:
    - matriz (list): La matriz a graficar.

    Returns:
    None
    """
    filas, columnas = len(matriz), len(matriz[0])

    x = np.arange(filas)
    y = np.arange(columnas)
    x, y = np.meshgrid(x, y)

    z = np.array(matriz)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_title("Solución analítica ecuación de Laplace")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('V(x,y)')

    plt.show()

calculo(60,60,10)
