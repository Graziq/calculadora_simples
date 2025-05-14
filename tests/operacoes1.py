class Calculadora:
    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b


if __name__ == "__main__":
    calc = Calculadora()

    print("Operações disponíveis: soma, subtracao")
    operacao = input("Digite a operação desejada: ").strip().lower()

    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        exit()

    if operacao == "soma":
        resultado = calc.somar(a, b)
        print(f"Resultado da soma: {resultado}")
    elif operacao == "subtracao":
        resultado = calc.subtrair(a, b)
        print(f"Resultado da subtração: {resultado}")
    else:
        print("Operação inválida. Use 'soma' ou 'subtracao'.")
