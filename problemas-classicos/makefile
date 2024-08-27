# Definição do compilador Python e diretório dos scripts
PYTHON=python3
SCRIPT_DIR=./src
DATA_DIR=../testes

# Declaração de Phony Targets para que 'make' saiba que esses não são arquivos
.PHONY: guloso backtracking

entrada:
	cd $(SCRIPT_DIR) && $(PYTHON) gerador_de_entrada.py

comparacao:
	cd $(SCRIPT_DIR) && $(PYTHON) comparacao.py

entrada_e_comparacao:
	cd $(SCRIPT_DIR) && $(PYTHON) gerador_de_entrada.py && $(PYTHON) comparacao.py
