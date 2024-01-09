# microservice-deploy-H3

Rapport mi-parcours

Le but du projet est de déployer une application de gestion d'inventaire. Par l'utilisation :
- 1 Dockerfile front => Application flask
- 1 Dockerfile back => SQL server
- => docker-compose.yml pour gerer les deux Dockerfile et le déploiement
- Utilisation d'un nginx quand il sera déployé sur azure
- (+) Implémentation de Kubernetes pour orchestrer les containers docker
- (+) Utilisation de graphana pour faire du monitoring
- (+) Mise en place d'un systeme de gestion de files d'attente
- (+) Mise en place de PowerBI pour une prise d'info via des graphiques


# Architecture

![Schema](https://github.com/BlazingBurn/Microservice_implement_stockManagement/assets/49305403/acc1462e-b6ef-46ef-a7fd-25d87e948d78)

# Route
    => Regarder dans le README.md flask_app

# PROBLEME RENCONTRE

Problemes qui ont ralenti => 
- PC perso qui on ralenti le developpement (Bug, freeze)
- Compatibilité dans le dockerfile entre le back et front (1j d'investigation pour résoudre le probleme)

# A FAIRE (Dans la semaine si le temps le permet)
- Déployé sur azure
- Ajouter kubernetes

# EXPLICATION BUILD/RUN PROJET

Le projet est build sur Azure et donc automatiquement.

Les liens pour acceder à l'application :
** Lien non disponible puisque l'application n'est plus accesible **