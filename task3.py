#Camila Richter

import math

class Task3:
    y_real = [100, 150, 200, 250, 300]
    y_prediccion = [110, 140, 210, 240, 500]

    def calcular_error_individual:
        n = len(y_real)
        errores = []

        for i in range(n):
            error = y_real[i] - y_pred[i]
            errores.append(error)
            
        return y_error
