import pandas as pd

def validar_entrada_numerica(mensaje, minimo=None, maximo=None):
    """Valida que la entrada sea un número dentro de un rango específico."""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

def validar_opcion(mensaje, opciones_validas):
    """Valida que la entrada sea una opción válida."""
    while True:
        opcion = input(mensaje).lower()
        if opcion in opciones_validas:
            return opcion
        print(f"Opción no válida. Las opciones permitidas son: {', '.join(opciones_validas)}")

def calcular_cuota_frances(importe_inicial, interes_anual, meses_restantes):
    """Calcula la cuota mensual usando el modelo francés."""
    interes_mensual = interes_anual / 12
    if interes_mensual == 0:
        return importe_inicial / meses_restantes
    cuota = (importe_inicial * interes_mensual) / (1 - (1 + interes_mensual) ** (-meses_restantes))
    return cuota

def calcular_amortizacion():
    # Entrada de datos básicos
    print("=== Calculadora de Amortización de Hipoteca ===")
    importe_inicial = validar_entrada_numerica("Importe inicial pendiente de la hipoteca: ", minimo=0)
    interes_anual = validar_entrada_numerica("Interés anual (%): ", minimo=0) / 100
    meses_restantes = int(validar_entrada_numerica("Número de meses restantes: ", minimo=1))

    # Calcular la cuota mensual con el modelo francés
    cuota_mensual_original = calcular_cuota_frances(importe_inicial, interes_anual, meses_restantes)
    print(f"\nLa cuota mensual calculada es: {cuota_mensual_original:.2f} €")

    # Entrada de amortización adicional
    print("\n¿Deseas añadir una amortización adicional? (1: Sí / 2: No): ")
    opcion = validar_opcion("", ["1", "2"])
    if opcion == "1":
        tipo_amortizacion = validar_opcion(
            "Tipo de amortización (1: Puntual / 2: Mensual / 3: Anual): ",
            ["1", "2", "3"]
        )
        if tipo_amortizacion == "1":
            amortizacion_adicional = validar_entrada_numerica("Cantidad puntual a amortizar: ", minimo=0)
        elif tipo_amortizacion == "2":
            amortizacion_adicional = validar_entrada_numerica("Cantidad mensual adicional a amortizar: ", minimo=0)
        elif tipo_amortizacion == "3":
            amortizacion_adicional = validar_entrada_numerica("Cantidad anual adicional a amortizar: ", minimo=0)

        # Elegir entre amortizar cuota o plazo
        tipo_amortizacion_final = validar_opcion(
            "¿Qué deseas reducir? (1: Cuota / 2: Plazo): ",
            ["1", "2"]
        )
    else:
        amortizacion_adicional = 0
        tipo_amortizacion_final = "2"  # Por defecto, reducir plazo si no hay amortización adicional

    # Preguntar si se desea mantener la suma de cuota + amortización constante
    mantener_pago_constante = False
    if tipo_amortizacion_final == "1":
        mantener_pago_constante = validar_opcion(
            "¿Deseas mantener la suma de cuota + amortización constante? (1: Sí / 2: No): ",
            ["1", "2"]
        ) == "1"

    # Cálculo de la amortización
    interes_mensual = interes_anual / 12
    saldo_pendiente = importe_inicial
    tabla_amortizacion = []
    pago_total_constante = cuota_mensual_original if mantener_pago_constante else None
    total_intereses_pagados = 0  # Variable para acumular los intereses totales

    for mes in range(1, meses_restantes + 1):
        # Aplicar amortización adicional
        if tipo_amortizacion == "1" and mes == 1:
            saldo_pendiente -= amortizacion_adicional
        elif tipo_amortizacion == "2":
            saldo_pendiente -= amortizacion_adicional
        elif tipo_amortizacion == "3" and mes % 12 == 0:
            saldo_pendiente -= amortizacion_adicional

        # Recalcular la cuota si se elige amortizar cuota
        if tipo_amortizacion_final == "1":
            cuota_mensual = calcular_cuota_frances(saldo_pendiente, interes_anual, meses_restantes - mes + 1)
        else:
            cuota_mensual = cuota_mensual_original

        # Calcular intereses y amortización
        interes_mes = saldo_pendiente * interes_mensual
        amortizacion_mes = cuota_mensual - interes_mes

        # Ajustar si se mantiene el pago total constante
        if mantener_pago_constante:
            amortizacion_mes += pago_total_constante - cuota_mensual
            cuota_mensual = pago_total_constante - amortizacion_mes

        # Actualizar saldo pendiente
        saldo_pendiente -= amortizacion_mes
        if saldo_pendiente < 0:
            saldo_pendiente = 0

        # Acumular intereses pagados
        total_intereses_pagados += interes_mes

        # Guardar datos en la tabla
        tabla_amortizacion.append({
            "Mes": mes,
            "Cuota": round(cuota_mensual, 2),
            "Intereses": round(interes_mes, 2),
            "Amortización": round(amortizacion_mes, 2),
            "Amortización Adicional": round(amortizacion_adicional, 2) if (
                (tipo_amortizacion == "1" and mes == 1) or
                (tipo_amortizacion == "2") or
                (tipo_amortizacion == "3" and mes % 12 == 0)
            ) else 0,
            "Saldo Pendiente": round(saldo_pendiente, 2),
            "Intereses Acumulados": round(total_intereses_pagados, 2)
        })

        # Si el saldo llega a cero, terminamos
        if saldo_pendiente == 0:
            break

    # Mostrar la tabla de amortización completa
    df = pd.DataFrame(tabla_amortizacion)

    # Configurar pandas para mostrar todas las filas y columnas
    pd.set_option('display.max_rows', None)  # Mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
    pd.set_option('display.width', 1000)  # Ajustar el ancho para evitar recortes

    print("\n=== Tabla de Amortización Completa ===")
    print(df)

    # Mostrar el total de intereses pagados
    print(f"\nTotal de intereses pagados: {total_intereses_pagados:.2f} €")

    # df.to_csv("tabla_amortizacion.csv", index=False)
# Ejecutar la aplicación
calcular_amortizacion()