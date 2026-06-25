# 📘 Assignment: Testes Automatizados e CI com pytest + GitHub Actions

## 🎯 Objective

Aprender a escrever testes automatizados com `pytest`, usar fixtures e parametrização, executar cobertura de testes, e integrar a suíte de testes em um pipeline de CI usando GitHub Actions.

## 📝 Tasks

### 🛠️ Escrever código e testes

#### Description
Implemente uma pequena biblioteca Python (`calc.py`) com funções utilitárias e escreva testes com `pytest` que verifiquem comportamento normal e casos de erro.

#### Requirements
Completed project should:

- Incluir um módulo `calc.py` com funções básicas (por exemplo, `add`, `sub`, `mul`, `div`).
- Escrever testes em `tests/` cobrindo entradas válidas, casos de borda e exceções (ex.: divisão por zero).
- Usar fixtures e pelo menos um teste parametrizado.
- Incluir um arquivo `requirements-dev.txt` listando `pytest` e dependências de teste.

#### Example commands
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
```

### 🛠️ Integrar com GitHub Actions (CI)

#### Description
Adicione um workflow que execute `pytest` em cada push e pull request em `main`.

#### Requirements

- Criar um arquivo de workflow em `.github/workflows/ci-python.yml` que execute os testes em Python 3.10+.
- O workflow deve instalar dependências e rodar `pytest`.

---

Place your solution files (`calc.py`, `tests/`, `requirements-dev.txt`) in this folder. Follow the example commands above to run tests locally.
