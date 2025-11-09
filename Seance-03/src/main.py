#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023

## Question 1
# création de src/data/
# on introduit le ficher "resultats-elections[...].csv"



## Question 2
# On introduit le fichier main.py


## Question 3
# Nous ouvrons le main.py dans VS Code


## Question 4

with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv", "r") as fichier :
    contenu = pd.read_csv(fichier)

table = pd.DataFrame(contenu)

print(table) #OPTIONNEL




## Question 5
# On créer des fonctions pour appeler plus facilement le code créé en séance 2 :
def dresserListeTypeColonnes(table):
    types_colonnes = [] #On crée une liste vide (on l'initialise)
    #Pour chaque colonne, 
    for nom_colonne in table.columns :
        element = table[nom_colonne][0]
        if type(element) == np.float64 :
            types_colonnes.append(float)

        elif type(element) == str :
            types_colonnes.append(str)

        elif type(element) == np.int64 :
            types_colonnes.append(int)

        elif type(element) == bool :
            types_colonnes.append(bool)

        else :
            types_colonnes.append(None)
    return types_colonnes


# Programme de la question 5
# on dresse la liste des types des colonnes
types_colonnes = dresserListeTypeColonnes(table)

colonnes = table.columns

liste_titres_col_quanti = []
moyennes = []
medianes = []
modes = []
ecarts_types = []
ecarts_absolus = []
etendues = []

for i in range(len(colonnes)):
    if types_colonnes[i] in [float, int]: # si la colonne est quantitative :
        # On enregistre le titre de la colonne traitée
        liste_titres_col_quanti.append(colonnes[i])
        # On isole la colonne traitée
        new_col = table[colonnes[i]]

        # On calcule et stocke la moyenne des valeurs de la colonne
        moy = new_col.mean()
        moyennes.append(round(float(moy), 2))

        # On calcule et stocke la médiane des valeurs de la colonne
        med = new_col.median()
        medianes.append(round(float(med), 2))

        # On calcule et stocke le mode des valeurs de la colonne
        mod = new_col.mode()
        modes.append(round(mod, 2))

        # On calcule et stocke l'ecart-type des valeurs de la colonne
        eca_typ = new_col.std()
        ecarts_types.append(round(float(eca_typ), 2))

        # On calcule et stocke l'écart absolu à la moyenne, des valeurs de la colonne
        #   La méthode .mad n'existe plus, on calcule donc manuellement :
        #   "la moyenne des [ecarts-absolus à la moyenne]"
        somme_eca_abs = 0
        for j in range(len(new_col)):
            somme_eca_abs += np.abs(moy - new_col[j])
        eca_abs = somme_eca_abs / len(new_col)
        ecarts_absolus.append(round(float(eca_abs), 2))

        # On calcule et stocke l'étendue des valeurs de la colonne
        eten = np.abs(new_col.max() - new_col.min())
        etendues.append(round(float(eten), 2))


## Question 6

print("liste_titres_col_quanti =", liste_titres_col_quanti)
print("moyennes =", moyennes)
print("medianes =", medianes)
#print("modes =", modes)
print("ecarts_types =", ecarts_types)
print("ecarts_absolus =", ecarts_absolus)
print("etendues =", etendues)



## Question 7
distances_interquart = []
distances_interdec   = []
for nom_colonne in liste_titres_col_quanti:
    new_col = table[nom_colonne]

    quart_25 = new_col.quantile(0.25)
    quart_75 = new_col.quantile(0.75)
    deci_10  = new_col.quantile(0.1)
    deci_90  = new_col.quantile(0.9)

    distances_interquart.append(round(float(quart_75 - quart_25),2))
    distances_interdec.append(round(float(deci_90 - deci_10), 2))


#OPTIONNEL :
print("distances_interquart =" ,distances_interquart)
print("distances_interdec =", distances_interdec)


## Question 8

for nom_colonne in liste_titres_col_quanti:
    plt.boxplot(table[nom_colonne])
    
    plt.title("Boite à moustache pour les valeurs de la colonne {}".format(nom_colonne)) #Titre principal
    plt.xlabel(nom_colonne) #Titre de l'axe vertical (X)
    plt.ylabel("Effectif")  #Titre de l'axe vertical (Y)

    plt.grid(True)              #Ajout de la grille

    #Sauvegarde du résultat 
    plt.savefig("./output/img/boite_moustache_pour_{}.png".format(nom_colonne))
    plt.close() #Fermeture 'propre' du graphe


## Question 9 
# C'est fait, on a bien le deuxième .csv dans le fichier data



## Question 10

with open("./data/island-index.csv", "r") as fichier :
    contenu = pd.read_csv(fichier)

iles = pd.DataFrame(contenu)

surfaces = iles["Surface (km²)"]

print(surfaces)

# Oranigramme :
# La surface est-elle inférieure à 10 ?
#   |
#   --OUI: On enregistre dans ]0,10]
#   |
#   --NON: La surface est-elle inférieure à 25 ?
#       |
#       --OUI: On enregistre dans ]10,25]
#       |
#       --NON: La surface est-elle inféreieure à 50 ?
#           |
#           --OUI: On enregistre dans ]25,50]
#           |
#           --NON: La surface est-elle inféreieure à 100 ?
#               |
#               etc...

compte_0_10       = 0
compte_10_25      = 0
compte_25_50      = 0
compte_50_100     = 0
compte_100_2500   = 0
compte_2500_5000  = 0
compte_5000_10000 = 0
compte_10000_INF  = 0

for surface in surfaces:
    if surface <= 10.0:
        compte_0_10 += 1
    elif surface <= 25.0:
        compte_10_25 += 1
    elif surface <= 50.0:
        compte_25_50 += 1
    elif surface <= 100.0:
        compte_50_100 += 1
    elif surface <= 2500.0:
        compte_100_2500 += 1
    elif surface <= 5000.0:
        compte_2500_5000 += 1
    elif surface <= 10000.0:
        compte_5000_10000 += 1
    else :
        compte_10000_INF += 1

print("Entre 0 et 10km², on dénombre {} îles."        .format(compte_0_10))
print("Entre 10 et 25km², on dénombre {} îles."       .format(compte_10_25))
print("Entre 25 et 50km², on dénombre {} îles."       .format(compte_25_50))
print("Entre 50 et 100km², on dénombre {} îles."      .format(compte_50_100))
print("Entre 100 et 2 500km², on dénombre {} îles."   .format(compte_100_2500))
print("Entre 2 500 et 5 000km², on dénombre {} îles." .format(compte_2500_5000))
print("Entre 5 000 et 10 000km², on dénombre {} îles.".format(compte_5000_10000))
print("Au delà de 10 000km², on dénombre {} îles."    .format(compte_10000_INF))