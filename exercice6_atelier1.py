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
    CYLINDRE_2000 = 2000
    NBRE_LITRE_PAR_KM_1 = 0.1
    NBRE_LITRE_PAR_KM_2 = 0.08
    SURCOUT_1 = 1.5
    SURCOUT_2 = 1.7 #un commentaire pour expliquer à quoi correspondent les surcoûts pourrait être utile
    
    if(type_carburant == TYPE_CARBURANT_ESSENCE or type_carburant == TYPE_CARBURANT_DIESEL):
        
    
        if (type_carburant == TYPE_CARBURANT_ESSENCE):
            if(cylindree > CYLINDRE_2000): 
                frais_mensuel=(NBRE_LITRE_PAR_KM_1*(nbre_km/12)*prix_carburant)*SURCOUT_1
            elif (cylindree < CYLINDRE_2000): #conditon inutile: si cylindre n'est pas plus petit que 2000,il sera forcément plus grand...
                #avec ces contdiions, tu risques d'avoir des erreurs si le cylindre est égal à 2000 (car tu traites seulement strictement inférieur et strictement supérieur...)
                frais_mensuel=(NBRE_LITRE_PAR_KM_2*(nbre_km/12)*prix_carburant)*SURCOUT_1
        else:
            frais_mensuel = NBRE_LITRE_PAR_KM_2*(nbre_km/12)*prix_carburant*SURCOUT_2
    else:
        frais_mensuel= "type_carburant non valide"
        
    return frais_mensuel

print(frais_mensuel(1200, "E", 2100, 1)) 

#15
