# Camila Richter
import math

def calcular_error_individual(y_real, y_pred):
    errores = []
    for i in range(len(y_real)):
        errores.append(y_real[i] - y_pred[i])
    return errores


def RMSE(y_real, y_pred):
    suma = 0
    for i in range(len(y_real)):
        error = y_real[i] - y_pred[i]
        suma += error ** 2
    return math.sqrt(suma / len(y_real))


def MAE(y_real, y_pred):
    suma = 0
    for i in range(len(y_real)):
        suma += abs(y_real[i] - y_pred[i])
    return suma / len(y_real)

    
