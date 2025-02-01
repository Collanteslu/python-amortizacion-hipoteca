# Calculadora de Amortización de Hipoteca

Este proyecto es una calculadora de amortización de hipotecas en Python que permite calcular la cuota mensual según el modelo francés y gestionar amortizaciones adicionales de manera puntual, mensual o anual.

## Características

- Cálculo de la cuota mensual de la hipoteca utilizando el **método francés**.
- Soporte para amortizaciones adicionales:
  - **Puntual**: Se realiza una amortización única.
  - **Mensual**: Se amortiza una cantidad fija cada mes.
  - **Anual**: Se realiza una amortización cada 12 meses.
- Elección entre reducir el **plazo** o la **cuota**.
- Opcion para **mantener el pago total constante** si se elige amortizar cuota.
- Generación de una **tabla de amortización completa** con detalles de intereses, cuota, amortización y saldo pendiente.
- Exportación de la tabla en formato **CSV**.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados:

- Python 3.x
- Pandas

Puedes instalar las dependencias necesarias con:

```sh
pip install pandas
```

## Instalación y Uso

1. **Clona el repositorio**
   ```sh
   git clone https://github.com/Collanteslu/python-amortizacion-hipoteca.git
   cd calculadora-hipoteca
   ```
2. **Ejecuta el script**
   ```sh
   python calculadora.py
   ```
3. **Sigue las instrucciones** en la consola para ingresar los datos de la hipoteca y amortizaciones adicionales.

## Ejemplo de Uso

```
=== Calculadora de Amortización de Hipoteca ===
Importe inicial pendiente de la hipoteca: 100000
Interés anual (%): 3.5
Número de meses restantes: 240

La cuota mensual calculada es: 579.96 €

¿Deseas añadir una amortización adicional? (1: Sí / 2: No): 1
Tipo de amortización (1: Puntual / 2: Mensual / 3: Anual): 2
Cantidad mensual adicional a amortizar: 100
¿Qué deseas reducir? (1: Cuota / 2: Plazo): 2

=== Tabla de Amortización Completa ===
(Mostrará la tabla con los detalles de cada mes)

Total de intereses pagados: 26,000.00 €
```

## Salida de Datos

El programa genera una tabla de amortización con las siguientes columnas:

- **Mes**: Número de mes.
- **Cuota**: Pago mensual.
- **Intereses**: Intereses pagados en ese mes.
- **Amortización**: Parte del capital que se paga en ese mes.
- **Amortización Adicional**: Monto adicional amortizado (si aplica).
- **Saldo Pendiente**: Capital restante por pagar.
- **Intereses Acumulados**: Total de intereses pagados hasta el momento.

La tabla se puede exportar a CSV descomentando la línea:

```python
# df.to_csv("tabla_amortizacion.csv", index=False)
```

## Contribución

Si quieres mejorar esta calculadora, sigue estos pasos:

1. **Haz un fork** del repositorio.
2. **Crea una rama** con tu nueva funcionalidad.
   ```sh
   git checkout -b nueva-funcionalidad
   ```
3. **Realiza los cambios y haz un commit.**
   ```sh
   git commit -m "Agregada nueva funcionalidad"
   ```
4. **Sube los cambios y crea un Pull Request.**
   ```sh
   git push origin nueva-funcionalidad
   ```

## Licencia

Este proyecto está licenciado bajo la MIT License. Ver [LICENSE](LICENSE) para más detalles.

