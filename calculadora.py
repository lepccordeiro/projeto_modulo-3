# Script calculadora.py
def main():
    # Entrada do primeiro número
    num1 = float(input("Digite o primeiro número: "))

    # Entrada do segundo número
    num2 = float(input("Digite o segundo número: "))

    # Escolha da operação
    op = input("Escolha uma operação (+, -, *, /): ")

    # Realizando a operação com condicional
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida!")
            return
    else:
        print("Operação inválida!")
        return

    # Exibindo o resultado
    print(f"Resultado: {resultado}")

# Executando a calculadora
if __name__ == "__main__":
    main()

