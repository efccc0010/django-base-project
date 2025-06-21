# Nombre del entorno virtual
VENV = env
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Crear entorno virtual y activar
init:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Ejecutar el servidor
run:
	$(PYTHON) manage.py runserver

# Aplicar migraciones
migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

# Crear superusuario
superuser:
	$(PYTHON) manage.py createsuperuser

# Probar conexión y shell
shell:
	$(PYTHON) manage.py shell

# Ejecutar pruebas
test:
	$(PYTHON) manage.py test

# Ver estado de migraciones
showmigrations:
	$(PYTHON) manage.py showmigrations

# Limpiar archivos pyc
clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

# Ejecutar el linter (si usas flake8, black, etc.)
lint:
	flake8 . || echo "Flake8 no está instalado"

# Reinstalar dependencias
reset:
	rm -rf $(VENV)
	make init

coverage:
	coverage run manage.py test
	coverage report

coverage-html:
	coverage html

lint:
	flake8 .

format:
	isort . && black .
