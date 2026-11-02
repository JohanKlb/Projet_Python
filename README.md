## Etudiant : Johan Kalbe | Groupe : B2

# Module : Outils Fondamentaux (Informatique & Mathématiques)

Ce dépôt contient l'ensemble de mes travaux pratiques (dossier `tp/`) ainsi que mon projet personnel de synthèse (dossier `projet/`).

## Présentation Détaillée du Projet (SBGI)

Le Simulateur Balistique et Géométrique Intelligent (SBGI) est une application Python développée dans le cadre du module Outils Fondamentaux. Son objectif principal est de modéliser une chaîne d'analyse complète, allant de la validation sécurisée des paramètres jusqu'à la vérification géométrique d'un impact balistique sur une cible mobile ou orientée.

Le projet a été conçu pour illustrer l'interconnexion entre plusieurs concepts mathématiques et informatiques étudiés en cours, sans s'appuyer sur des fonctions automatisées natives (comme `abs()` ou `reversed()`), afin de privilégier la réimplémentation des algorithmes fondamentaux.

---

### Architecture et Enchaînement des Fonctionnalités

Le workflow du projet s'articule autour de 4 grandes étapes exécutées séquentiellement :

#### 1. Validation Arithmétique et Sécurité
Avant d'autoriser le lancement de la simulation, le programme effectue un contrôle d'accès basé sur la théorie des nombres :
* Test de primalité optimisé : Vérification de la validité d'une clé de sécurité numérique (ex: 100003). L'algorithme teste les diviseurs jusqu'à la racine carrée pour garantir une exécution rapide.

#### 2. Modélisation Balistique et Recherche de Racines
La trajectoire de l'objet est représentée par une fonction polynomiale du second degré.
* Évaluation par le schéma de Horner : Calcul stable et optimisé évitant les calculs de puissances coûteux.
* Calcul de la dérivée polynomiale : Détermination analytique pour obtenir la pente de la trajectoire.
* Résolution par la méthode de Newton : Recherche numérique itérative du point d'impact au sol. L'algorithme converge avec une précision de 10^-12 en un nombre restreint d'itérations.

#### 3. Algèbre Linéaire et Transformations Cibles
La zone cible initiale est un polygone à deux dimensions défini par ses sommets. Pour simuler une cible réorientée ou inclinée :
* Matrice de transformation homogène 3x3 : Construction d'une matrice de rotation 2D en coordonnées homogènes.
* Multiplication matricielle : Application de la transformation simultanément sur les sommets de la zone cible et sur le point d'impact calculé.
* Calcul d'aire (Formule du lacet) : Évaluation de la superficie du polygone avant et après transformation pour vérifier la conservation des surfaces.

#### 4. Analyse Géométrique de l'Impact (Ray-Casting)
La dernière étape détermine si le tir a atteint sa cible :
* Algorithme du lancer de rayon (Ray-Casting) : Détermination de l'appartenance d'un point à un polygone en comptant le nombre d'intersections entre un demi-axe horizontal virtuel partant du point d'impact et les arêtes de la cible. Si le nombre d'intersections est impair, l'impact est validé dans la cible.

---

### Structure du Code Source

Le projet adopte une architecture modulaire répartie en plusieurs fichiers :
* `outils.py` : La bibliothèque mathématique du projet. Elle regroupe toutes les fonctions de calcul (valeur absolue personnalisée, test de primalité, Horner, Newton, produit matriciel, formule du lacet, Ray-Casting).
* `main.py` : Le point d'entrée exécutable. Il orchestre le scénario complet, gère les flux d'entrée/sortie dans la console et affiche les résultats d'impact.
* `test_projet.py` : Un script de test d'intégration automatisé qui valide la précision et la cohésion de l'ensemble de la chaîne de calcul.
