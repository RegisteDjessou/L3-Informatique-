"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul de salaire
"""


def salaire(salaire_horaire: float, nombre_heures:float)-> float : #attention, pour tout l'atelier 1 on ne devait pas mettre de return ni de paramètres dans nos fonctions
    
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

#Plutôt que de faire des tests qui se baladent comme ça, tu peux faire directement une fonction "test", qui fait tous les tests d'un coup
