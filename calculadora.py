

from operaciones import operaciones

def main():
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        operador = input("Ingresa el operador (+, -, *, /, **, //): ")

        if operador == '+':
            resultado = operaciones.suma(a, b)
        elif operador == '-':
            resultado = operaciones.resta(a, b)
        elif operador == '*':
            resultado = operaciones.multiplicacion(a, b)
        elif operador == '/':
            resultado = operaciones.division(a, b)
        elif operador == '**':
            resultado = operaciones.potencia(a, b)
        elif operador == '//':
            resultado = operaciones.division_entera(a, b)
        else:
            raise ValueError("Operador no válido.")

        print(f"Resultado: {resultado}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
