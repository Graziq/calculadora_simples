# Projeto: Calculadora Simples com Prefect, Python (OO), Docker e GitHub

## Visão Geral
Este projeto implementa uma **calculadora simples** orientada a objetos (OO) com operações de **soma e subtração**, utilizando a orquestração de tarefas com **Prefect**, empacotamento com **Docker** e versionamento com **GitHub**. O código está modularizado em pacotes Python, com testes e fluxo separados por pasta.

---

## Problema
Criar uma aplicação básica e reutilizável para realizar operações matemáticas, com arquitetura orientada a objetos e estrutura preparada para orquestração e automação.

---

## Solução
- Estrutura modular com classes Python
- Operações encapsuladas em uma classe `Calculadora`
- Fluxo de execução com Prefect em `flows/flow_versao1.py`
- Testes separados em `tests/`
- Infraestrutura com Docker
- Integração com GitHub

---

## Objetivos
- Realizar soma e subtração
- Encapsular lógica com orientação a objetos
- Modularizar a aplicação
- Orquestrar com Prefect
- Automatizar com Docker
- Versionar no GitHub

---

## Estrutura do Projeto

CALCULADORA_SIMPLES/
├── .github/workflows/ # (CI/CD futuramente)
├── docs/
│ └── readme.txt
├── flows/
│ └── flow_versao1.py # Fluxo principal com Prefect
├── infra/ # Infraestrutura (Docker etc.)
├── src/
│ └── calculadora/
│ └── operacoes.py # Classe Calculadora com métodos OO
├── tests/
│ ├── operacoes.py
│ ├── operacoes1.py
│ └── operacoes2.py
├── .gitignore
├── .prefectignore
├── prefect.yaml
├── README.md
├── requirements.txt

## Próximos Passos
-> Adicionar testes unitários com pytest

-> Incluir multiplicação e divisão na classe Calculadora