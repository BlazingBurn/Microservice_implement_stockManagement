# microservice-deploy-H3

Rapport mi-parcours

Le but du projet est de déployer une application de gestion d'inventaire. Par l'utilisation :
- 1 Dockerfile front => Il s'agit d'une application flask
- 1 Dockerfile back => SQL server
- => docker-compose.yml pour gerer les deux Dockerfile et le déploiment
- Utilisation d'un nginx quand il sera déployé sur azure
- (+) Implémentation de Kubernetes pour orchestrer les containers docker
- (+) Utilisation de graphana pour faire du monitoring
- (+) Mise en place d'un systeme de gestion de files d'attente
