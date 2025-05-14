# -*- coding: utf-8 -*-

class Calculadora:
    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b


if __name__ == "__main__":
    operacao = "subtracao"  # ou "soma"
    a = 10.9
    b = 4

    calc = Calculadora()

    if operacao == "soma":
        resultado = calc.somar(a, b)
        print(f"Resultado da soma: {resultado}")
    elif operacao == "subtracao":
        resultado = calc.subtrair(a, b)
        print(f"Resultado da subtração: {resultado}")
    else:
        print("Operação inválida.")