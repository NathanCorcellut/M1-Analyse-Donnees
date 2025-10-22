#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

## Question 1 ##
#Ouverture du fichier "pib-vs-energie.csv"
data = pd.DataFrame(ouvrirUnFichier("./data/pib-vs-energie.csv"))
#print(data) #OPTIONNEL: aperçu du tableau entier

#On isole les colonnes PIB_2022 et Utilisation_d_energie_2022
pib_2022 =     list(pd.DataFrame(ouvrirUnFichier("./data/pib-vs-energie.csv"))["PIB_2022"])
energie_2022 = list(pd.DataFrame(ouvrirUnFichier("./data/pib-vs-energie.csv"))["Utilisation_d_energie_2022"])

#OPTIONNEL: aperçu des listes brutes (non testées)
#print("\033[96m pib_2022 =", pib_2022) 
#print("\033[95m energie_2022 =", energie_2022, "\033[0m")



## Question 2 ##
#Visualisation des données
print("Visualisation des données")
#Pour résoudre le problème posé dans la question 2, il faut utiliser l'opérateur NaN avec la méthode qui le teste issue de la bibliothèque Numpy dans une boucle.
pib_2022_propre = []
energie_2022_propre = []
for element in range (0, len(pib_2022)):
    if (np.isnan(pib_2022[element]) == False) and (np.isnan(energie_2022[element]) == False) :
        pib_2022_propre.append(pib_2022[element])
        energie_2022_propre.append(energie_2022[element])

#OPTIONNEL: aperçu des listes testées
print("\033[96m pib_2022_propre =", pib_2022_propre) 
print("\033[95m energie_2022_propre =", energie_2022_propre, "\033[0m")

#Calcul de la régression linéaire pour la méthode des moindres carrées
print("Calcul de la régression linéaire pour la méthode des moindres carrées")



#Calcul du coefficient de corrélation simple de Pearson
print("Calcul du coefficient de corrélation simple de Pearson")