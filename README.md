# MyPyMonitor
[English version below]
A la recherche d'un moyen simple d'afficher des données en temps réels entre différents programmes Python? Alors ce projet vous sera utile! L'objectif est de permettre de transmettre et d'afficher automatiquement les données le plus facilement possible!
Pour en savoir plus, il n'y a qu'à lire la suite de ce readme et de découvrir les exemples!

[English version]
Looking for an easy way to plot data in real time from other Python programs? If so, this project will be useful! The aim is to provide a way to exchange and plot easily several data in real time!
To know more about it, please see at the end of this readme and look at the examples!

## Sommaire

## I/ Utilisation du module zenoh: avantages et utilité
Le module zenoh est un module permettant d'utiliser le protocole ZENOH (pour Zero Overhead Network Protocol). On présente ici les aspects qui nous intéressent. Pour plus d'informations, il faudra se reporter à la documentation zenoh.io .

### 1/ Installation
Pour l'instant, il suffit simplement d'utiliser une installation pip pour que tout fonctionne! Si ce n'est pas le cas, se reporter à la documentation. Cette partie sera mise à jour au fur et à mesure que le projet avance et que je rencontre des problèmes d'utilisation!

```cmd
pip install eclipse-zenoh
```

D'autres modules "secondaires" sont à installer (pour gérer l'interface graphique). Pour les installer, entrez la commande:
```cmd
pip install -r requirement.txt
```

### 2/ Avantages et utilité
TODO

## II/ Comment utiliser MyPyMonitor
Pour utiliser MyPyMonitor, rien de plus simple. Il suffit tout simplement d'incluer les lignes suivantes dans le programme dont vous voulez afficher les données!

1. Importer le module zenoh:
   ```python
   import zenoh
   ```

2. Initialiser la connection zenoh
   ```python
   # Initialize Zenoh
   print("[INFO] Initialisation of zenoh")
   z = zenoh.open()
   ```

3. Initialiser le client zenoh
   Il s'agit ici d'indiquer sur quelle adresse les données seront envoyées. Vous pouvez choisir n'importe quelle adresse!
   ```python
   print("[INFO] Initialisation of the publisher")
   pub = z.declare_publisher('demo/example/hello')
   ```

4. Envoyer les données
   Vous pouvez maintenant envoyer les données que vous voulez!
   ```python
   pub.put(to_send)
   ```
   Ici, la variable to_send représente les données à envoyer!

## III/ Roadmap du projet
Voici les fonctionnalités qui devraient être développées dans ce projet:
- gestion de sources multiples de données
- scan du réseau zenoh
- sélection facile des données à afficher
- permettre l'enregistrement de données
- création d'une console pour envoyer des données et/ou commandes
- GUI sous la forme de docker
- enregistrement de templates d'affichage pour en faciliter les affichages
- pouvoir lancer des programmes depuis le GUI

# MyPyMonitor (English version)
TODO (if you absolutely want it, tell me and i will do it as soon as possible)
## Summary

## I/ Use of Zenoh: how to

## II/ How to use MyPyMonitor

## III/ Roadmap