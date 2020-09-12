"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul les frais mensuels d'utilisation d'une voiture
"""

def frais_mensuel(nbre_km: float, type_carburant: str, cylindree: int, prix_carburant: float):
    """Calcul les frais mensuels d'utilisation d'une voiture"""
    TYPE_CARBURANT_ESSENCE = "E"
    TYPE_CARBURANT_DIESEL = "D"
    
    if(type_carburant == TYPE_CARBURANT_ESSENCE or type_carburant == TYPE_CARBURANT_DIESEL):
        CYLINDRE_2000 = 2000
        NBRE_LITRE_PAR_KM_1 = 0.1
        NBRE_LITRE_PAR_KM_2 = 0.08
        SURCOUT_1 = 1.5
        SURCOUT_2 = 1.7
    
        if (type_carburant == TYPE_CARBURANT_ESSENCE):
            if(cylindree > CYLINDRE_2000):
                frais_mensuel=(NBRE_LITRE_PAR_KM_1*(nbre_km/12)*prix_carburant)*SURCOUT_1
            elif (cylindree < CYLINDRE_2000):
                frais_mensuel=(NBRE_LITRE_PAR_KM_2*(nbre_km/12)*prix_carburant)*SURCOUT_1
        else:
            frais_mensuel = NBRE_LITRE_PAR_KM_2*(nbre_km/12)*prix_carburant*SURCOUT_2
    else:
        frais_mensuel= "type_carburant non valide"
        
    return frais_mensuel

print(frais_mensuel(1200, "E", 2100, 1))

#15