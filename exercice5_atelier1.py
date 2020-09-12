"""
#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul le cout annuel de la place au port d'un voilier
"""

def port():
    """ Calcul le cout annuel de la place au port d'un voilier """
    
    LONGUEUR_VOILIER_1 = 5
    COUT_1 = 100
    LONGUEUR_VOILIER_2 = 10
    COUT_2 = 200
    LONGUEUR_VOILIER_3 = 12
    COUT_3 = 400
    COUT_4 = 600
    CATEGORIE_1 = 1
    TAXE_SPECIALE_1 = 100
    CATEGORIE_2 = 2
    TAXE_SPECIALE_2 = 150
    CATEGORIE_3 = 3
    TAXE_SPECIALE_3 = 250
    
    nom_voilier = input("Entrez un nom de voilier :")
    
    longueur_voilier =float(input("Entrez la longueur du voilier :"))
    
    categorie = int(input("Entrez la categorie du voilier :"))
    
    #cout mensuel que doit payer le proprio du voilier
   
    if(longueur_voilier < LONGUEUR_VOILIER_1):
        #longueur_voilier < 5
        cout_mensuel = COUT_1
        
    elif (longueur_voilier <= LONGUEUR_VOILIER_2):
        cout_mensuel = COUT_2
    elif(longueur_voilier <= LONGUEUR_VOILIER_3):
        cout_mensuel = COUT_3
    else : 
        cout_mensuel = COUT_4
        
    #taxe speciale anuelle que doit payer le proprio du voilier
    
    if(categorie == CATEGORIE_1 or categorie == CATEGORIE_2 or categorie== CATEGORIE_3):
        if(categorie == CATEGORIE_1):
            taxe_speciale_annuelle = TAXE_SPECIALE_1
        elif(categorie == CATEGORIE_2):
            taxe_speciale_annuelle = TAXE_SPECIALE_2
        else :
            taxe_speciale_annuelle = TAXE_SPECIALE_3
    else :   
        message = "Categorie invalide"
        
    #cout annuel de la place au port 
    cout_annuel = taxe_speciale_annuelle + 12*cout_mensuel

    
    message = "Le cout annuel d'une place obtenu au port pour le voilier " + nom_voilier + " est de " + str(cout_annuel) + " euros" 
    return message

print(port())
    
    

    