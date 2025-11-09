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



