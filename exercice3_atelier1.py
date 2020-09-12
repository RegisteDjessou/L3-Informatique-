"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Verifie si quelqu'un est imposable ou non
"""

def impots(age: int, sexe: str):
    """ Verifie si quelqu'un est imposable ou non """
    SEXE_MASCULIN = "M" 
    SEXE_FEMININ = "F"
    MIN_IMPOSABLE_H = 20
    MIN_IMPOSABLE_F = 18
    MAX_IMPOSABLE_F = 35
    
    if(sexe == SEXE_MASCULIN or sexe == SEXE_FEMININ):
        if( (sexe == SEXE_MASCULIN and age >MIN_IMPOSABLE_H) or (sexe == SEXE_FEMININ and age >=MIN_IMPOSABLE_F and age <=MAX_IMPOSABLE_F )):
            #ça aurait pu être intéressant de commenter pour expliquer en français les conditions pour vérifier si une personne est imposable ou pas
            resultat = "Paie les impots"
        else:
            resultat = "Ne paie pas les impots"
    else:
        resultat= "Votre sexe est incorrect"

    return resultat

print(impots(16, "F"))
print(impots(30, "M"))



