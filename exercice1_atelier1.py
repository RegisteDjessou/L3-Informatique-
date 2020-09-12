"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul de salaire
"""


def salaire(salaire_horaire: float, nombre_heures:float)-> float :
    
    """Calcul de salaire en fontion du nombre d'heures"""
    
    PALIER_1 = 160
    PALIER_2 = 200
    MAJORATION_1 = 1.25
    MAJORATION_2 = 1.5
    
    
    if nombre_heures <= PALIER_1:
        salaire_mensuel = salaire_horaire*nombre_heures
    else:
        salaire_mensuel = salaire_horaire*PALIER_1
        if nombre_heures <= PALIER_2 :
        
           salaire_mensuel += (salaire_horaire*(nombre_heures-PALIER_1))*MAJORATION_1
        else:
            
            salaire_mensuel += salaire_horaire*(PALIER_2-PALIER_1)*MAJORATION_1
            salaire_mensuel += (salaire_horaire*(nombre_heures-PALIER_2))*MAJORATION_2
    
    return salaire_mensuel


print("Test1", salaire(1,220))
print("Test2", salaire(30,200))