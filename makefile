.PHONY: help run test migrate clean

help:
	@echo "Makefile pour un projet Django"
	@echo
	@echo "Commandes disponibles:"
	@echo "  make run    : Lancer le serveur Django"
	@echo "  make test   : Exécuter les tests Django"
	@echo "  make migrate : Exécuter les migrations Django"
	@echo "  make clean  : Supprimer les fichiers générés"

run:
	python3.11 manage.py runserver

test:
	python3.11 manage.py test

migrate:
    python3.11 manage.py migrate

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.log' -delete
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf *.log