# Module : Outils Fondamentaux (Informatique & Mathématiques)

Ce dépôt contient le dossier `tp/` regroupant les travaux pratiques du module ainsi que le dossier `projet/` dédié au projet de synthèse.

## Structure du Dépôt

- `tp/` : Réponses aux exercices et carnets de TP du module.
- `projet/` : Contient le script unique du projet (`main.py`).

---

## Projet : Simulateur Balistique et Géométrique Intelligent (SBGI)

### Description du sujet
Ce projet propose une approche unifiée de modélisation mathématique et informatique. Il simule le comportement d'une trajectoire balistique modélisée par un polynôme, calcule précisément son point d'impact à l'aide de méthodes itératives, puis évalue l'atteinte d'une zone cible soumise à des transformations géométriques et matricielles.

Les notions fondamentales du module s'entrecroisent tout au long du script :
- **Arithmétique & Sécurité** : Validation préalable des paramètres numériques par test de primalité.
- **Polynômes & Analyse numérique** : Évaluation stable des fonctions par le schéma de Horner et recherche de racines par la méthode de Newton.
- **Algèbre linéaire & Géométrie** : Manipulation de matrices homogènes 3x3 pour effectuer des rotations, combinée à l'analyse de polygones (formule du lacet et test d'appartenance par *Ray-Casting*).

### Comment lancer le projet
Ouvrez un terminal à la racine du dépôt, puis exécutez les commandes suivantes :

```bash
cd projet
python main.py
