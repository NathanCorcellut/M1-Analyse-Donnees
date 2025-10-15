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
        for element1 in range(0, len(ordre2)):
            for element2 in range(0, len(ordre1)):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1)):
            for element2 in range(0, len(ordre2)):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element1][1]])
    return classement

#Partie sur les îles

## Question 2 ##
#Ouverture du fichier "island-index.csv"
iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv")) 
#print(iles) #OPTIONNEL: aperçu du tableau entier

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().



## Question 3 ##
#On isole la colonne "Surface (km²)" en la castant en list()
surfaces = list(iles["Surface (km²)"])
#print(surfaces) #OPTIONNEL: aperçu de la liste créée /!\ Affichage terminal volumineux

#Ajout des valeurs de surface des continents
surfaces.append(float(85545323)) #Asie / Afrique / Europe
surfaces.append(float(37856841)) #Amérique
surfaces.append(float( 7768030)) #Antarctique
surfaces.append(float( 7605049)) #Australie
#print(surfaces) #OPTIONNEL: aperçu de la liste complétée /!\ Affichage terminal volumineux



## Question 4 ##
#On ordonne la liste "surfaces" (de façon décroissante) 
surfaces_decroissant = ordreDecroissant(surfaces)
#print(surfaces_decroissant) #OPTIONNEL: aperçu de la liste complétée et triée /!\ Affichage terminal volumineux



## Question 5 ##
#On crée la liste des rangs (qui seront les abscisses du graphe)
rangs = list(range(1, len(surfaces_decroissant)+1)) #On a: rangs = [1, 2, 3, ... , 84223]

#Génération du graphe
plt.plot(rangs, surfaces_decroissant, "o-") #Génération du graphe

#Ajout des titres et de la grille
plt.title("Q5 - Loi rang-taille des terres émergées") #Titre principal
plt.xlabel("Rang")          #Titre de l'axe horizontal (X)
plt.ylabel("Surface (km²)") #Titre de l'axe vertical (Y)
plt.grid(True)              #Ajout de la grille

#Sauvegarde du résultat 
plt.savefig("./output/Q5-loi_rang-taille_terres.png") #sous le nom "Q5-loi_rang-taille_terres.png"
plt.close() #Fermeture 'propre' du graphe



## Question 6 ##
#Passage des valeurs au logarithme
surf_decr_log = conversionLog(surfaces_decroissant) #Pour les surfaces (axe Y)
rangs_log = conversionLog(rangs)                    #Pour les rangs (axe X)

#Génération du graphe corrigé
plt.plot(rangs_log, surf_decr_log, "o-")

#Ajout des titres et de la grille
plt.title("Q6 - Loi rang-taille (log-log) des terres émergées") #Titre principal
plt.xlabel("log(Rang)")    #Titre de l'axe horizontal (X)
plt.ylabel("log(Surface)") #Titre de l'axe vertical (Y)
plt.grid(True)             #Ajout de la grille

#Sauvegarde du résultat 
plt.savefig("./output/Q6-loi_rang-taille_log-log_terres.png") #sous le nom "Q6-loi_rang-taille_log-log_terres.png"
plt.close() #Fermeture 'propre' du graphe



## Question 7 ##
# Non, on ne peut pas faire un test (statistique) sur les rangs. 
# Les rangs ne sont pas issus d'un échantillon aléatoire, mais ils sont générés par
# une simple numérotation ordonnée (1er, 2e, 3e, ...). 
# En effet, nous avons créé la liste des rangs après avoir trié la liste des surfaces. 
# La corrélation entre le rang et la taille est donc évidente, car forcée "par construction".
# Le rang et la taille ne sont donc pas des variables indépendantes issues de mesures distinctes.
# Cela implique qu'on ne peut pas appliquer un test de corrélation (au sens statistique) entre le rang et la taille. 





#Partie sur les populations des États du monde

## Question 9 ##
#Ouverture du fichier "Le-Monde-HS-Etats-du-monde-2007-2025.csv"
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))
print(monde) #OPTIONNEL: aperçu du tableau entier

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().