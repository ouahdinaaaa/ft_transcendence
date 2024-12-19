##################################################################################
### Nous utilisons l'image de base Python et nous installons les dépendances   ###
### définies dans le fichier requirements.txt. Le serveur Django est configuré ###
### pour être accessible depuis l'extérieur du conteneur sur le port 8000.     ###
##################################################################################

# Utilise l'image officielle Python comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement les dépendances
COPY ./backend/requirements.txt /app/

# Copier manage.py et tout le reste du dossier backend
COPY ./backend /app/


# Mettre à jour pip à la dernière version et installer les dépendances Python spécifiées dans requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

# Exposer le port 8000 pour que l'application Django soit accessible sur ce port
EXPOSE 8000

# Lancer le serveur Django en écoutant sur l'adresse 0.0.0.0 (pour qu'il soit accessible depuis l'extérieur du conteneur)
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]

