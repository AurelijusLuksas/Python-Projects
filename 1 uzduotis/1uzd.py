import numpy as np
from sympy import symbols, diff, integrate, exp
import matplotlib.pyplot as plt


def firstTask():
    interval = np.linspace(-1.3,2.5,64)
    print(interval)

def secondTask():
    array = np.array([1, 2, 3, 4])
    N = 3
    repeatingArray = np.tile(array, N)
    print(repeatingArray)

def thirdTask():
    array = np.array([3])
    N = 4
    repeatingArray = np.repeat(array, N)
    print(repeatingArray)

def fourthTask():
    matrixArray = np.zeros((8, 8), int)
    padddedArray = np.pad(matrixArray, pad_width=1, mode='constant', constant_values=1)
    print(padddedArray)

def fifthTask():
    checkerBoard = np.zeros((8, 8), int)
    checkerBoard[1::2, ::2] = 1
    checkerBoard[::2, 1::2] = 1
    print(checkerBoard)

def sixthTask():
    array = np.zeros((8, 8), int)

    for i in range(8):
        for j in range(8):
            array[i][j] = i + j
    print(array)
    

def seventhTask():
    array = np.random.rand(5, 5)
    sortedArray = array[array[:, 1].argsort()]
    print(sortedArray)

def eigthTask():
    matrix = np.random.rand(5, 5)
    realValue, realVector = np.linalg.eig(matrix)
    print(realValue)
    print(realVector)

def ninthTask():

    p = np.poly1d([0.5, 5, 4])
    pDerivative = p.deriv()
    print(pDerivative)

    x = symbols('x')
    f = 0.5*x**2 + 5*x + 4
    fDerivative = diff(f, x)
    print(fDerivative)

def tenthTask():
    x = symbols('x')
    f = exp(-x)
    indefIntegral = integrate(f, x)
    print(indefIntegral)

    defInteg = integrate(f, (x, 0, 1))
    print(defInteg)

def eleventhTask():
    theta = np.linspace(0, 2*np.pi, 1000)
    r = 1 - np.sin(theta)

    plt.figure(figsize=(6, 6))
    plt.polar(theta, r)
    plt.show()

def twelvethTask(V, D):
    numbers = np.random.normal(loc=V, scale=np.sqrt(D), size=1000)

    plt.hist(numbers, bins=30, density=True)
    plt.show()

firstTask()
secondTask()
thirdTask()
fourthTask()
fifthTask()
sixthTask()
seventhTask()
eigthTask()
ninthTask()
tenthTask()
eleventhTask()
twelvethTask(13, 1)
    





