##################################################################################
### Nous utilisons l'image officielle PostgreSQL et définissons les variables  ###
### d'environnement pour la création de la base de données et de l'utilisateur.###
### Le port 5432 est exposé pour permettre les connexions à la base de données.###
##################################################################################

# Utilise l'image officielle de PostgreSQL
FROM postgres:14-alpine

# Configurer les variables d'environnement pour la base de données PostgreSQL
# POSTGRES_USER : Utilisateur de la base de données
# POSTGRES_PASSWORD : Mot de passe pour l'utilisateur PostgreSQL
# POSTGRES_DB : Nom de la base de données à créer lors du démarrage
ENV POSTGRES_USER=yourusername
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_DB=yourdatabase

# Exposer le port 5432, utilisé par PostgreSQL pour les connexions à la base de données
EXPOSE 5432
