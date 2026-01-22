from task3 import MAE, RMSE, calcular_error_individual

def main():
    y_real = [100, 150, 200, 250, 300]
    y_pred = [110, 140, 210, 240, 500]

    errores = calcular_error_individual(y_real, y_pred)
    mae_value = MAE(y_real, y_pred)
    rmse_value = RMSE(y_real, y_pred)

    print("Errores individuales:", errores)
    print("MAE:", mae_value)
    print("RMSE:", rmse_value)

if __name__ == "__main__":
    main()
