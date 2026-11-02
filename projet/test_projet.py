"""
Fichier de test d'intégration : test_projet.py
Description : Teste le projet entier (l'intégration entre outils.py et main.py)
en exécutant le scénario global et en vérifiant chaque étape de la simulation.
"""

import math
from outils import (
    est_premier,
    evaluer_horner,
    newton_racine,
    aire_polygone,
    produit_matrices,
    appliquer_transformation,
    point_dans_polygone
)

def tester_projet_entier():
    print("=== LANCEMENT DES TESTS DE L'INTÉGRATION DU PROJET ===")

    # 1. Test de la validation de sécurité (Arithmétique)
    cle = 100003
    assert est_premier(cle) == True, "Échec : La clé de sécurité devrait être valide."
    print(" [OK] Étape 1 : Validation de la clé d'accès")

    # 2. Test du calcul du point d'impact (Polynômes + Newton)
    # Trajectoire : P(x) = -0.1x^2 + 2x + 5
    P = [5.0, 2.0, -0.1]
    impact_x, tours = newton_racine(P, depart=15.0)
    
    # Vérification que le polynôme s'annule bien en impact_x (P(impact_x) ~= 0)
    valeur_a_l_impact = evaluer_horner(P, impact_x)
    assert abs(valeur_a_l_impact) < 1e-9, "Échec : Le point d'impact calculé n'annule pas le polynôme."
    assert impact_x > 20.0, "Échec : La portée calculée semble incorrecte."
    print(f" [OK] Étape 2 : Simulation balistique (impact trouvé à x = {impact_x:.4f} en {tours} itérations)")

    # 3. Test géométrique de la zone cible initiale (ajustée pour englober l'impact)
    zone_cible = [(20.0, -2.0), (25.0, -2.0), (25.0, 3.0), (20.0, 3.0)]
    superficie = aire_polygone(zone_cible)
    assert superficie == 25.0, f"Échec : L'aire devrait être de 25.0, obtenu : {superficie}"
    print(f" [OK] Étape 3 : Calcul d'aire de la zone cible ({superficie} unités²)")

    # 4. Test des transformations matricielles (Algèbre linéaire)
    angle_deg = 5
    rad = math.radians(angle_deg)
    c, s = math.cos(rad), math.sin(rad)
    matrice_rot = [[c, -s, 0], [s, c, 0], [0, 0, 1]]

    zone_transformee = [appliquer_transformation(pt, matrice_rot) for pt in zone_cible]
    impact_transforme = appliquer_transformation((impact_x, 0.0), matrice_rot)
    
    # L'aire doit être préservée après une rotation
    superficie_rot = aire_polygone(zone_transformee)
    assert abs(superficie_rot - 25.0) < 1e-9, "Échec : La rotation a altéré l'aire de la cible."
    print(" [OK] Étape 4 : Application de la transformation matricielle (Rotation de 5°)")

    # 5. Test d'impact géométrique (Ray-Casting)
    touche = point_dans_polygone(impact_transforme, zone_transformee)
    assert touche == True, "Échec : L'impact devrait toucher la cible transformée."
    print(" [OK] Étape 5 : Test d'atteinte de la cible transformée (Résultat : TOUCHÉ)")

    print("Tous les tests d'intégration du projet ont réussi avec succès !")

if __name__ == "__main__":
    tester_projet_entier()
