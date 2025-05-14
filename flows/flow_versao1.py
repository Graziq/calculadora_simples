from prefect import task, flow
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from calculadora.operacoes import Calculadora 

@task
def somar(a: float, b: float):
    calc = Calculadora(a,b)
    resultado = calc.somar()
    print(f"Resultado da soma: {resultado}")
    return resultado

@task
def subtrair(a: float, b: float):
    calc = Calculadora(a,b)
    resultado = calc.subtrair()
    print(f"Resultado da subtracao: {resultado}")
    return resultado

@flow(name="Fluxo de Operações Básicas")
def fluxo_operacoes():
    a = 10
    b = 5
    resultado_soma = somar(a,b) #apenas p/ armazenar
    resultado_subtracao = subtrair(a,b)

if __name__ == "__main__":
    fluxo_operacoes()