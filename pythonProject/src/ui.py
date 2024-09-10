from api import consultar_datos_suelos, calcular_mediana


def interfaz_usuario():
    print("Bienvenido a la consulta de propiedades edáficas de suelos.")

    # Entrada de datos por el usuario
    departamento = input("Ingrese el departamento: ")
    municipio = input("Ingrese el municipio: ")
    cultivo = input("Ingrese el cultivo: ")
    limite = int(input("Ingrese el número de registros a consultar (e.g. 10, 100): "))

    # Consulta los datos desde la API
    datos = consultar_datos_suelos(departamento, municipio, cultivo, limite)

    # Mostrar los resultados
    if not datos.empty:
        print(f"Se han encontrado {len(datos)} registros.")
        columnas_edaficas = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']  # Ajusta las columnas según los datos reales
        medianas = calcular_mediana(datos, columnas_edaficas)

        if medianas is not None:
            print("\nMedianas de las propiedades edáficas consultadas:")
            print(f"pH: {medianas['ph_agua_suelo_2_5_1_0']}, Fósforo (P): {medianas['f_sforo_p_bray_ii_mg_kg']}, Potasio (K): {medianas['potasio_k_intercambiable_cmol_kg']}")
        else:
            print("No se encontraron registros con valores en las columnas especificadas.")
    else:
        print("No se encontraron datos con los criterios proporcionados.")
