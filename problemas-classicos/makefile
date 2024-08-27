PYTHON=python3
PIP=pip3
SCRIPT_DIR=./src
DATA_DIR=../testes

# Declaração de Phony Targets para que 'make' saiba que esses não são arquivos
.PHONY: entrada comparacao entrada_e_comparacao install_dependencies

entrada:
	cd $(SCRIPT_DIR) && $(PYTHON) gerador_de_entrada.py

comparacao:
	cd $(SCRIPT_DIR) && $(PYTHON) comparacao.py

entrada_e_comparacao:
	cd $(SCRIPT_DIR) && $(PYTHON) gerador_de_entrada.py && $(PYTHON) comparacao.py

install_dependencies:
	sudo apt-get update
	sudo apt-get install -y python3 python3-pip
	$(PIP) install matplotlib pandas
