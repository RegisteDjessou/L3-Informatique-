"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Precise type de caractere 
"""

def caracteres(caractere: str):
    """ Retourne le type du caractere entré """
    
    MIN_CHIFFRE = 48
    MAX_CHIFFRE = 57
    MIN_LETTRE_MAJ = 65
    MAX_LETTRE_MAJ = 90
    MIN_LETTRE_MIN = 97
    MAX_LETTRE_MIN = 122
     
    if (ord(caractere)>=MIN_CHIFFRE and ord(caractere)<=MAX_CHIFFRE):
        resultat = "chiffre"
    elif (ord(caractere)>=MIN_LETTRE_MAJ and ord(caractere)<=MAX_LETTRE_MAJ):
        resultat = "lettre majuscule"
    elif (ord(caractere)>=MIN_LETTRE_MIN and ord(caractere)<=MAX_LETTRE_MIN):
        resultat = "lettre miniscule"
    else:
        resultat = "caractere special"
        
    return resultat

print(caracteres("A"))
print(caracteres("a"))
print(caracteres("1"))
print(caracteres("/"))
