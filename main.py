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

    print(
        "\nEl RMSE penaliza más el error del último dato porque al elevar los errores al cuadrado "
        "los errores grandes aumentan de forma desproporcionada su contribución al resultado final. "
        "Esta diferencia es importante en aplicaciones críticas, como la predicción de "
        "dosis de medicamentos, donde un error grande puede tener consecuencias graves para la salud del "
        "paciente, por lo que es preferible usar métricas que penalicen este tipo de fallos."
    )

if __name__ == "__main__":
    main()
