# Projet Cantine - Guide d'Installation et de Test

Bienvenue dans le projet **Cantine**. Ce projet est une application web de gestion de cantine scolaire développée avec Django.

## Prérequis

- [Python 3.12+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/) (optionnel, pour cloner le projet)
- [pip](https://pip.pypa.io/en/stable/installation/) (Gestionnaire de paquets Python)

## Installation

Suivez ces étapes pour installer et configurer le projet localement :

### 1. Cloner le dépôt

2. Créer et activer un environnement virtuel
python -m venv env
Activez l'environnement virtuel :
Sur Windows :
env\Scripts\activate
Sur macOS/Linux :
source env/bin/activate

3. Installer les dépendances du fichier à partir requirements.txt
pip install -r requirements.txt

4. Configuration de la base de données
Assurez-vous d'avoir MySQL installé et configuré sur votre machine.
Créez une base de données nommée cantine_bd dans MySQL.
Ensuite, modifiez les paramètres de connexion à la base de données dans le fichier settings.py

5. Appliquer les migrations avec python manage.py makemigrations puis python manage.py migrate

6. Lancer le serveur de développement avec python manage.py runserver
