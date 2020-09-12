import math
"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Associer un tarif d'assurance a un client"""

def assurance():
    """Associer un tarif d'assurance a un client"""
    
    AGE_25 = 25
    DUREE_PERMIS_2_ANS = 2
    TARIF_BLEU = 4
    TARIF_VERT = 3
    TARIF_ORANGE = 2
    TARIF_ROUGE = 1
    REFUSEE = 0
    NOMBRE_ACCIDENT_1 = 1
    NOMBRE_ACCIDENT_2 = 2
    
    age = int(input("Entrez votre age:"))
    duree_permis = int(input("Depuis quand etes vous titulaire de votre permis? :"))
    nombre_accident = int(input("Combien d'acidents avez vous provoque?:"))
    nombre_annee_assurance = int(input("Entrez le nombre d'annees.....:")) 
    
    if(age < AGE_25):   
        if(duree_permis < DUREE_PERMIS_2_ANS):
            if(nombre_accident < NOMBRE_ACCIDENT_1):
                tarif = TARIF_ROUGE
            else:   
                tarif = REFUSEE
        else:  
            if(nombre_accident < NOMBRE_ACCIDENT_1):  
                tarif = TARIF_ORANGE
            elif(nombre_accident == NOMBRE_ACCIDENT_1):  
                tarif = TARIF_ROUGE
            else:  
                tarif=0
    else: 
        
         
        if(duree_permis < DUREE_PERMIS_2_ANS):
            if(nombre_accident < NOMBRE_ACCIDENT_1):  
                tarif = TARIF_ORANGE
            elif(nombre_accident == NOMBRE_ACCIDENT_1):  
                tarif = TARIF_ROUGE
            else:  
                tarif = REFUSEE
        else:  
            if(nombre_accident < NOMBRE_ACCIDENT_1):
                tarif = TARIF_VERT
            elif(nombre_accident == NOMBRE_ACCIDENT_1):  
                tarif = TARIF_ORANGE
            elif(nombre_accident == NOMBRE_ACCIDENT_2):  
                tarif = TARIF_ROUGE
            else:  
                tarif = REFUSEE
                
    if(nombre_annee_assurance>1 and tarif!=REFUSEE):
        tarif +=1
    
    if(tarif == REFUSEE):
        tarif="Assurance refusee"
    elif(tarif == TARIF_ROUGE):  
        tarif="rouge"
    elif(tarif == TARIF_ORANGE):
        tarif="orange"
    elif(tarif == TARIF_VERT):   
        tarif="vert"
    else:
        tarif="bleu"
    
    return tarif

print(assurance())
         