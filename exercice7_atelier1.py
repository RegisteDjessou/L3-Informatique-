
"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Traite du resultat du candidat 1 a une election"""

def election():
    MINIMUM_1ER = 50
    MINIMUM_BELOTAGE = 12.5 #"ballotage"
    
    """  Traite du resultat du candidat 1 a une election """
    candidat1 = float(input("Entrez le score du candidat 1: "))
    candidat2 = float(input("Entrez le score du candidat 2: "))
    candidat3 = float(input("Entrez le score du candidat 3: "))
    candidat4 = float(input("Entrez le score du candidat 4: "))
    
    maximum = max(candidat1,candidat2,candidat3,candidat4)
    
    if(maximum == candidat1):
        if(maximum > MINIMUM_1ER):  
             message = "Candidat 1 elu"
        else :
            if( candidat1 >= MINIMUM_BELOTAGE):  
               message = "Candidat 1 balotage favorable"
            else:    
                message = "Candidat 1 perdu"
    else:  
        if(maximum > MINIMUM_1ER or candidat1 < MINIMUM_BELOTAGE):   
            message = "Candidat 1 perdu"
        else:   
            message = "Candidat 1 en balotage defavorable"
    return message

print(election()) 
            
