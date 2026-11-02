# Etudiant : Johan Kalbe      Groupe : B2

# Module : Outils Fondamentaux (Informatique & Mathématiques)

Ce dépôt contient l'ensemble de mes travaux pratiques (dossier `tp/`) ainsi que mon projet personnel de synthèse (dossier `projet/`).

## Structure du Dépôt

- `tp/` : Contient les carnets de TP réalisés au cours du module.
- `projet/` : Contient le code source du projet de synthèse, divisé en deux modules pour plus de lisibilité :
  - `outils.py` : Regroupe les fonctions mathématiques, l'arithmétique, l'évaluation de polynômes, les matrices et la géométrie.
  - `main.py` : Le fichier principal qui orchestre et exécute la simulation.

---

## Projet : Simulateur Balistique et Géométrique Intelligent (SBGI)

### Ce que fait le projet
Le programme modélise un cas pratique complet croisant plusieurs notions fondamentales du module :
1. **Arithmétique** : Validation de la sécurité par test de primalité.
2. **Polynômes & Analyse numérique** : Évaluation de fonctions par le schéma de Horner et résolution de trajectoires par la méthode de **Newton** (sans fonctions natives interdites comme `abs` ou `reversed`).
3. **Algèbre linéaire & Géométrie** : Manipulation de matrices homogènes 3x3 pour des transformations géométriques, calcul d'aires par la formule du lacet et test d'appartenance par lancer de rayon (*Ray-Casting*).

### Comment le lancer
Assurez-vous d'avoir Python installé. Ouvrez un terminal, placez-vous dans le dossier du projet et exécutez le fichier principal :

```bash
cd projet
python main.py
