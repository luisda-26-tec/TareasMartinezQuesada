def operation_selector(num1, num2, op): #inicialización de parámetros para función
    resultado = None

    # Sanity checks
    # ----------------------------------
    if not isinstance(num1, int):#si no es entero código de error -50 y None
        return -50, resultado

    if isinstance(num1, bool):
        return -50, resultado #si es booleano igual error -50 y None

    if not isinstance(op, str):
        return -60, resultado #si el operador no es string, código -60 y None

    if not isinstance(num2, int):#si no es entero código de error -50 y None
        return -50, resultado

    if isinstance(num2, bool):
        return -50, resultado #si es booleano igual error -50 y None

    if op not in ["+", "-", "*", "&"]:
        return -70, resultado #si el operador no es un carácter seleccionado, código -70 y None

    # Realiza la operacion
    # ----------------------------------
    if op == "+":
        resultado = num1 + num2 #suma
    elif op == "-":
        resultado = num1 - num2 #resta
    elif op == "*":
        resultado = num1 * num2 #multiplica
    else:
        resultado = num1 & num2 #AND logica

    return 0, resultado


def calculo_promedio(lista_valores):
    # Ciclo for para la potencia
    resultado = None

    # Sanity checks
    # ----------------------------------
    if len(lista_valores) > 10:
        return -90, resultado #lista con más de 10 valores genera error

    for i in lista_valores: 
        if (not isinstance(i, int)) and (not isinstance(i, float)): #si no es entero ni flotante, código error -80 y None
            return -80, resultado

        if isinstance(i, bool): # si es booleano error -80 y None
            return -80, resultado

    # Calculo de promedio
    # ----------------------------------
    resultado = sum(lista_valores)/len(lista_valores) #promedio es suma de valores entre cantidad de los mismos

    return 0, resultado
