"""
Projet : Simulateur Balistique et Géométrique Intelligent (SBGI)
Fichier principal : main.py
Description : Script d'exécution principal faisant appel aux fonctions du module outils.py.
"""

import math
from outils import (
    est_premier,
    newton_racine,
    aire_polygone,
    appliquer_transformation,
    point_dans_polygone
)

def main():
    print("=== SIMULATEUR BALISTIQUE ET GÉOMÉTRIQUE INTELLIGENT (SBGI) ===")
    
    # 1. Validation de la clé de sécurité par arithmétique
    cle_securite = 100003
    print(f"\n[Validation] Vérification du protocole avec la clé {cle_securite}...")
    if not est_premier(cle_securite):
        print("Erreur : Clé non sécurisée.")
        return
    print(" -> Clé validée avec succès.")

    # 2. Modélisation de la trajectoire et recherche de racines
    # Trajectoire définie par le polynôme P(x) = -0.1x^2 + 2x + 5
    P = [5.0, 2.0, -0.1]
    print("\n[Simulation] Calcul du point d'impact de la trajectoire...")
    
    impact_x, iterations = newton_racine(P, depart=15.0)
    point_impact = (impact_x, 0.0)
    print(f" -> Impact détecté en x = {impact_x:.4f} (résolu en {iterations} itérations).")

    # 3. Analyse géométrique de la cible et transformations matricielles
    zone_cible = [(15.0, 0.0), (22.0, 0.0), (22.0, 5.0), (15.0, 5.0)]
    print(f"\n[Géométrie] Analyse de la zone cible initiale (Aire : {aire_polygone(zone_cible)} unités²)...")

    # Application d'une rotation de 45 degrés via une matrice homogène 3x3
    angle_deg = 45
    rad = math.radians(angle_deg)
    c, s = math.cos(rad), math.sin(rad)
    matrice_rot = [[c, -s, 0], [s, c, 0], [0, 0, 1]]

    zone_transformee = [appliquer_transformation(pt, matrice_rot) for pt in zone_cible]
    impact_transforme = appliquer_transformation(point_impact, matrice_rot)

    # 4. Vérification finale de l'atteinte de la cible transformée
    touche = point_dans_polygone(impact_transforme, zone_transformee)
    print(f" -> Point d'impact après rotation : ({impact_transforme[0]:.2f}, {impact_transforme[1]:.2f})")
    print(f" -> La cible transformée est-elle atteinte ? {'OUI' if touche else 'NON'}")

    print("\n=== FIN DE LA SIMULATION ===")

if __name__ == "__main__":
    main()
