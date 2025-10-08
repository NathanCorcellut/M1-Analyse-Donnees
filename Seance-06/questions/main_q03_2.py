#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

#Fonction pour ouvrir les fichiers
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Fonction pour convertir les données en données logarithmiques
def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

#Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

#Fonction pour obtenir le classement des listes spécifiques aux populations
def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

#Fonction pour obtenir l'ordre défini entre deux classements (listes spécifiques aux populations)
def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

#Partie sur les îles

## Question 2 ##
iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv"))
#print(iles)


## Question 3 ##
##On isole la colonne "Surface (km²)"
surfaces_iles = iles["Surface (km²)"]
#print(surfaces_iles)

##On repart du fichier, on y ajoute les surfaces des continents, puis on isole la colonne "Surface (km²)"
terres = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv")) #On ouvre à nouveau le fichier
terres.loc[len(terres)] = [None, "Asie / Afrique / Europe", None, None, None, None, None, float(85545323),  None, None] #Ajout après la dernière ligne
terres.loc[len(terres)] = [None, "Amérique",                None, None, None, None, None, float(37856841),  None, None] #Ajout après la nouvelle dernière ligne
terres.loc[len(terres)] = [None, "Antarctique",             None, None, None, None, None, float(7768030),   None, None] #Ajout après la nouvelle dernière ligne
terres.loc[len(terres)] = [None, "Australie",               None, None, None, None, None, float(7605049),   None, None] #Ajout après la nouvelle dernière ligne
surfaces_terrestres = terres["Surface (km²)"] #Isolement de la colonne "Surface (km²)"
print(surfaces_terrestres)


#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().


#Partie sur les populations des États du monde
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
#monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().