#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

## Question 1 ##
# Nous avons créé le dossier "data" et y avons introduit le fichier "resultats-elections-presidentielles-2022-1er-tour.csv"



## Question 2 ##
# Nous avons introduit le fichier "main.py"



## Question 3 ##
# Nous travaillons dans l'éditeur de code 'VS Code'



## Question 4 ##
# Ouverture du fichier "resultats-elections-presidentielles-2022-1er-tour.csv",
# puis lecture de son contenu
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier) #'pd.read_csv()' est la méthode "read_csv()" de la bibliothèque "Pandas",
                                   # celle-ci permet de lire les fichiers au format C.S.V.


## Question 5 ##
# Affichage sur le terminal de la variable "contenu"
table = pd.DataFrame(contenu) #'pd.DataFrame()' est la méthode "DataFrame()" de la bibliothèque "Pandas",
                              # celle-ci permet de structurer l'affichage des données (Data) - de façon bien rangée, comme un tableau (Frame)
print(table)



## Question 6 ##
# Mesure du nombre de lignes et de colonnes par la fonction native "len()"
nb_lignes =   len(table)
nb_colonnes = len(table.columns)

# Affichage du résultat
reponse = "Le tableau de données contient {} lignes et {} colonnes."
print(reponse.format(nb_lignes, nb_colonnes)) # la méthode "format()" va injecter les variables dans la chaine de caractère,
                                              # respectivement aux endroits indiqués par '{}'

                                        

## Question 7 ##
# liste =[]
# pour chaque colonne :
#     if isFloat :
#         liste.append(float)
#     elif isBool :
#         liste.appends(bool)
#

#OU ALORS :
#     liste.append(typeof)

