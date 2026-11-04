# Todo Actions

Lista de tarefas simples em Python, usada para explorar testes automatizados com GitHub Actions.

## O programa

A classe `TodoList` (em [todo.py](todo.py)) permite:

- adicionar tarefas (título vazio gera `ValueError`);
- remover e concluir tarefas pelo id (id inexistente gera `KeyError`);
- listar todas as tarefas ou apenas as pendentes.

Os 8 testes de unidade, escritos com [pytest](https://pytest.org), estão em [test_todo.py](test_todo.py).

## Rodando localmente

```bash
pip install -r requirements.txt
python -m pytest -v
```

## GitHub Actions

O workflow está em [.github/workflows/ci.yml](.github/workflows/ci.yml) e roda a cada `push` e `pull request`.

Ele usa uma **matriz** (`strategy.matrix`) que combina:

- **Sistemas operacionais:** `ubuntu-latest`, `macos-latest` e `windows-latest`;
- **Versões do Python:** 3.11, 3.12 e 3.13.

Isso gera 9 jobs, e cada um executa estes passos:

1. `actions/checkout` baixa o código;
2. `actions/setup-python` instala a versão do Python da matriz;
3. `pip install -r requirements.txt` instala o pytest;
4. `python -m pytest -v` roda os testes.

Com `fail-fast: false`, uma combinação que falha não cancela as outras, e dá para ver o resultado de todas.
