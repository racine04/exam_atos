# Projet Cantine - Guide d'Installation et de Test

Bienvenue dans le projet **Cantine**. Ce projet est une application web de gestion de cantine scolaire développée avec Django.

## Prérequis

Avant de commencer, assurez-vous que vous avez les éléments suivants installés sur votre machine :

- [Python 3.12+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/) (optionnel, pour cloner le projet)
- [pip](https://pip.pypa.io/en/stable/installation/) (Gestionnaire de paquets Python)

## Installation

Suivez ces étapes pour installer et configurer le projet localement :

### 1. Cloner le dépôt

Clonez ce dépôt en utilisant Git, ou téléchargez-le en tant qu'archive ZIP :

```bash
git clone https://votre-lien-vers-le-repo.git
cd votre-repo
2. Créer et activer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances du projet :

bash
Copy code
python -m venv env
Activez l'environnement virtuel :

Sur Windows :
bash
Copy code
env\Scripts\activate
Sur macOS/Linux :
bash
Copy code
source env/bin/activate
3. Installer les dépendances
Installez les dépendances nécessaires à partir du fichier requirements.txt :

bash
Copy code
pip install -r requirements.txt
Les modules principaux installés sont :

django-crispy-forms
django-bootstrap4
pymysql
4. Configuration de la base de données
Assurez-vous d'avoir MySQL installé et configuré sur votre machine.

Créez une base de données nommée cantine_bd dans MySQL.
Vous pouvez le faire avec la commande suivante dans MySQL :

sql
Copy code
CREATE DATABASE cantine_bd;
Ensuite, modifiez les paramètres de connexion à la base de données dans le fichier settings.py :

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cantine_bd',
        'USER': 'votre_nom_utilisateur_mysql',
        'PASSWORD': 'votre_mot_de_passe_mysql',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Appliquer les migrations
Exécutez les migrations pour configurer la base de données :

bash
Copy code
python manage.py migrate
6. Créer un superutilisateur (optionnel)
Si vous souhaitez accéder à l'interface d'administration de Django, vous devez créer un superutilisateur :

bash
Copy code
python manage.py createsuperuser
7. Lancer le serveur de développement
Vous pouvez maintenant lancer le serveur de développement :

bash
Copy code
python manage.py runserver