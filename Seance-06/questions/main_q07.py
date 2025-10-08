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
#print(surfaces_terrestres)


## Question 4 ##
##On ordonne la liste surfaces_terrestres (de facon décroissante) 
list_surf_terr_decr = ordreDecroissant(list(surfaces_terrestres))
#print(list_surf_terr_decr)


## Question 5 ##
rangs = list(range(1, len(list_surf_terr_decr) +1)) #Liste pour l'axe des abscisses, on a rangs = [1,2,3, ... , 84223]
plt.plot(rangs, list_surf_terr_decr, "o-") #Génération du graphe

plt.title("Q5 - Loi rang-taille des terres") #Ajout du titre
plt.xlabel("Rang")          #Ajout du titre de l'axe X
plt.ylabel("Surface (km²)") #Ajout du titre de l'axe Y
plt.grid(True)              #Ajout de la grille

plt.savefig("./output/Q5_loi_rang_taille_terres.png") #Sauvegarde du résultat sous le nom "Q5_loi_rang_taille_terres.png"
plt.close() #Fermeture propre du graphe


## Question 6 ##
list_surf_log = conversionLog(list_surf_terr_decr) #Passage au logarithme des valeurs de surface (axe Y)
rangs_log = conversionLog(rangs)                   #Passage au logarithme des valeurs de rang (axe X)
plt.plot(rangs_log, list_surf_log, "o-") #Génération du nouveau graphe

plt.title("Q6 — Loi rang-taille (log-log) des terres") #Ajout du titre
plt.xlabel("log(Rang)")    #Ajout du titre de l'axe X
plt.ylabel("log(Surface)") #Ajout du titre de l'axe Y
plt.grid(True)             #Ajout de la grille
plt.savefig("./output/Q6_loi_rang-taille_log-log_terres.png") #Sauvegarde du résultat sous le nom "Q6_loi_rang-taille_log-log_terres.png"
plt.close() #Fermeture propre du graphe


## Question 7 ##
# Non, on ne peut pas faire un test (statistique) sur les rangs. 
# En effet, les rangs ne sont pas issus d'un échantillon aléatoire, mais ils sont générés par une simple numérotation ordonée (1er, 2e, 3e, ...).
# Ainsi, on ne peut pas leur appliquer de test (comme par exemple ceux de Spearman ou Wilcoxon)


#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().


#Partie sur les populations des États du monde
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
#monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().