#  Simulateur de robot autonome en entrepôt

## Description
Ce projet simule un robot autonome qui doit récupérer des colis 
et les déposer à une zone d'arrivée, en trouvant automatiquement 
le chemin le plus court grâce à l'algorithme A*, un des plus perfomants pour ce genre de tâche.

Je l'ai créé pour approfondir mes connaissances en Python, 
notamment sur le parcours de graphes représentés par une matrice. 
A* m'intéressait particulièrement car j'avais déjà étudié Dijkstra sur d'autres de mes projets
et je voulais comprendre comment l'heuristique fonctionnait et améliorait les performances.
Ce projet m'a en tout prit environ 3 jours a développer.

## Fonctionnement
- Le robot part de son point de départ
- Il visite chaque point de récupération dans l'ordre
- Il dépose les colis à la zone d'arrivée
- Le chemin jaune représente la trajectoire calculée par A*

##  Technologies et algo

- **Python** — langage principal
- **Pygame** — simulation visuelle
- **A* (A-star)** — algorithme de pathfinding
- **Heuristique de Manhattan** — optimisation de la recherche
- **Matrice 2D** — représentation de l'environnement
- **Programmation orientée objet** — architecture modulaire
- **Autonomous navigation** — navigation autonome
- **Path planning** — planification de trajectoire

## Personnaliser l'entrepôt
Tout se modifie dans `data/entrepot.json` :
- `etageres` : coordonnées des cases bloquées `[colonne, ligne]`
- `point_recup` : positions de récupération des colis
- `depart` : position de départ du robot
- `arrivee` : zone de dépôt des colis

⚠️ Ne placez pas deux éléments sur la même case sinon le script crashera

## Installation
-> `requirements.txt` pour voir les dépendances nécessaires.

## Ce qui est prévu d'ici quelques semaines 
- Génération aléatoire des positions (étagere, zone de recup,zone d'arrivee) pour avoir plus de facilitée a voir l'efficatité du A* sans devoir modifier json a chaque fois
- Pause/reprise de la simulation