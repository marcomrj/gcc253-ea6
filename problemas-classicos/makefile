# Definição do compilador Python e diretório dos scripts
PYTHON=python3
SCRIPT_DIR=./src
DATA_DIR=../testes

# Declaração de Phony Targets para que 'make' saiba que esses não são arquivos
.PHONY: guloso backtracking

# Target para executar o script guloso.py
guloso:
	cd $(SCRIPT_DIR) && $(PYTHON) guloso.py

# Target para executar o script backtracking.py
backtracking:
	cd $(SCRIPT_DIR) && $(PYTHON) backtracking.py

entrada:
	cd $(SCRIPT_DIR) && $(PYTHON) gerador_de_entrada.py