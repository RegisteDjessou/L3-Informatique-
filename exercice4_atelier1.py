"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul la facture en fonction du nombre de copies 
"""

def reprographie(nombre_photocopies: int):
    """ Calcul la facture en fonction du nombre de copies """
     
    PRIX1=0.1
    SEUIL_PRIX1=10
    PRIX2=0.09
    SEUIL_PRIX2=20
    PRIX3=0.08
    
    if(nombre_photocopies <= SEUIL_PRIX1):
        facture =PRIX1* nombre_photocopies
    elif(nombre_photocopies <=(SEUIL_PRIX1+SEUIL_PRIX2)):    
        facture = (SEUIL_PRIX1*PRIX1) + (SEUIL_PRIX1+SEUIL_PRIX2)*(nombre_photocopies - SEUIL_PRIX1)
    else:   
        facture =(PRIX1*SEUIL_PRIX1) + (PRIX2*SEUIL_PRIX2) + PRIX3*(nombre_photocopies - (SEUIL_PRIX1+SEUIL_PRIX2))
    return facture

print(reprographie(31))