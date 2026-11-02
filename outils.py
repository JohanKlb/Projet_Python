"""
Module : Outils Mathématiques et Géométriques (outils.py)
Description : Regroupe les fonctions mathématiques de base, d'arithmétique,
d'analyse numérique (Horner, Newton), d'algèbre linéaire et de géométrie.
"""

import math

def valeur_absolue(x):
    """Calcule la valeur absolue d'un nombre sans utiliser abs()."""
    if x < 0:
        return -x
    return x

def presque_egaux(a, b, tolerance=1e-9):
    """Compare deux flottants en évitant les erreurs d'accumulation."""
    return valeur_absolue(a - b) <= tolerance

def est_premier(n):
    """Teste si un entier est premier pour valider les paramètres de sécurité."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def evaluer_horner(P, x):
    """Évalue un polynôme P en x de manière stable via le schéma de Horner (sans reversed)."""
    total = 0
    # On parcourt la liste des coefficients du dernier au premier par les indices
    for i in range(len(P) - 1, -1, -1):
        total = total * x + P[i]
    return total

def deriver_poly(P):
    """Renvoie les coefficients du polynôme dérivé."""
    return [i * P[i] for i in range(1, len(P))]

def newton_racine(P, depart, tolerance=1e-12, max_tours=100):
    """Trouve une racine du polynôme par la méthode de Newton."""
    derivee = deriver_poly(P)
    x = float(depart)
    for tour in range(max_tours):
        valeur = evaluer_horner(P, x)
        pente = evaluer_horner(derivee, x)
        if presque_egaux(pente, 0):
            raise ZeroDivisionError("Tangente horizontale : Newton bloque.")
        suivant = x - valeur / pente
        if valeur_absolue(suivant - x) <= tolerance:
            return suivant, tour + 1
        x = suivant
    raise RuntimeError("Non-convergence de Newton.")

def produit_matrices(A, B):
    """Multiplie deux matrices (listes de listes)."""
    n, p = len(A), len(A[0])
    q = len(B[0])
    C = [[0] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

def appliquer_transformation(point, matrice_3x3):
    """Applique une matrice de transformation homogène 3x3 à un point (x, y)."""
    x, y = point
    vect = [[x], [y], [1]]
    res = produit_matrices(matrice_3x3, vect)
    return (res[0][0], res[1][0])

def aire_polygone(polygone):
    """Calcule l'aire d'un polygone par la formule du lacet."""
    somme = 0
    n = len(polygone)
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        somme += x1 * y2 - x2 * y1
    return valeur_absolue(somme) / 2

def point_dans_polygone(P, polygone):
    """Test d'appartenance par lancer de rayon (Ray-Casting)."""
    x, y = P
    n = len(polygone)
    croisements = 0
    for i in range(n):
        (x1, y1), (x2, y2) = polygone[i], polygone[(i + 1) % n]
        if (y1 <= y) != (y2 <= y):
            if x1 + (y - y1) * (x2 - x1) / (y2 - y1) > x:
                croisements += 1
    return croisements % 2 == 1
