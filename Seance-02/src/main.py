#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

## Question 1 ##
# Dans le fichier "src", nous avons créé le dossier "data" et y avons introduit le fichier "resultats-elections-presidentielles-2022-1er-tour.csv"



## Question 2 ##
# Dans le fichier "src", nous avons introduit le fichier "main.py"



## Question 3 ##
# Nous travaillons dans l'éditeur de code 'VS Code'



## Question 4 ##
# Ouverture du fichier "resultats-elections-presidentielles-2022-1er-tour.csv",
# puis lecture de son contenu
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier) #'pd.read_csv()' est la méthode "read_csv()" de la bibliothèque "Pandas",
                                   # celle-ci permet de lire les fichiers au format C.S.V.



## Question 5 ##
# Dans le terminal, on affiche la variable "contenu"
table = pd.DataFrame(contenu) #'pd.DataFrame()' est la méthode "DataFrame()" de la bibliothèque "Pandas",
                              # celle-ci permet de structurer l'affichage des données (Data) - de façon bien rangée, comme un tableau (Frame)
print(table) #Affichage


## Question 6 ##
# Mesure du nombre de lignes et de colonnes par la fonction native "len()"
nb_lignes =   len(table)
nb_colonnes = len(table.columns) #'table.columns' est la liste des titres des colonnes
#print("table.columns =", table.columns) #OPTIONNEL: pour voir de quoi on parle

# Affichage du résultat
reponse = "Le tableau de données contient {} lignes et {} colonnes."
print(reponse.format(nb_lignes, nb_colonnes)) # la méthode "format()" va injecter les variables dans la chaîne de caractère,
                                              # respectivement aux endroits indiqués par '{}'

                                        

## Question 7 ##
# On dresse une liste qui renseigne le type de chaque colonne
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

    print("table[{}][0] = ".format(nom_colonne), element, "--> est de type :", type(element))

#OPTIONNEL:
print(types_colonnes)



## Question 8 ##
# Affichage du nom des colonnes avec la méthode "head()"
print(table.head(0)) #noter qu'elle s'utilise ainsi : [pd.DataFrame].head(n)
                     # (avec n le nombre de lignes à afficher)



## Question 9 ##
inscrits = table["Inscrits"]
print(inscrits)


## Question 10 ## 
# Pour chaque colonne :
#   isoler la colonne et cast en list
#   faire pd.sum de cette list

colonnes = table.columns
liste_sommes = []
for i in range(len(colonnes)):
    new_col = table[colonnes[i]]

    if types_colonnes[i] == int:
        liste_sommes.append(int(new_col.sum()))
    
    elif types_colonnes[i] == float:
        liste_sommes.append(float(new_col.sum()))

print(liste_sommes)



## Question 11

idx = table ["Code du département"]
X = table ["Inscrits"]
Y = table ["Abstentions"]
for i in range(len(idx)):

    plt.bar(["Inscrits", "Votants"], [X[i], Y[i]])
    #Ajout des titres et de la grille
    plt.title("Inscrits VS Votants dans le {}".format(idx[i])) #Titre principal
    plt.ylabel("Nombre") #Titre de l'axe vertical (Y)
    plt.grid(True)              #Ajout de la grille

    #Sauvegarde du résultat 
    plt.savefig("./output/images_Q11/ins_vs_vot_dep_{}.png".format(idx[i])) #sous le nom "Q5-loi_rang-taille_terres.png"
    plt.close() #Fermeture 'propre' du graphe   




## Question 12

# SEE MAELYS FILE

## 13

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import ceil


n = len(inscrits)

# Freedman-Diaconis pour nb de bins (optionnel)
iqr = inscrits.quantile(0.75) - inscrits.quantile(0.25)
if iqr == 0:
    nb_bins = 56
else:
    h = 2 * iqr / (n ** (1/3))
    if h <= 0:
        nb_bins = 30
    else:
        nb_bins = int(ceil((inscrits.max() - inscrits.min()) / h))

# Tracé de l'histogramme normalisé (aire = 1)
plt.figure(figsize=(8,5))
plt.hist(inscrits, bins=nb_bins, density=True, alpha=0.7)  # density=True => aire totale = 1
plt.xlabel('Nombre d\'inscrits')
plt.ylabel('Densité')
plt.title('Histogramme de la distribution des inscrits (aire = 1)')
# options : moyenne et médiane
plt.axvline(inscrits.mean(), color='k', linestyle='--', label=f'Moyenne = {inscrits.mean():.0f}')
plt.axvline(inscrits.median(), color='r', linestyle=':', label=f'Médiane = {inscrits.median():.0f}')
plt.legend()
plt.tight_layout()
plt.savefig('./output/images_Q13/hist_inscrits.png', dpi=150)
plt.show()

# Option : KDE (si scipy/numpy ok)
try:
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(inscrits)
    xs = np.linspace(inscrits.min(), inscrits.max(), 200)
    plt.figure(figsize=(8,4))
    plt.hist(inscrits, bins=nb_bins, density=True, alpha=0.5)
    plt.plot(xs, kde(xs))
    plt.title('Histogramme + KDE')
    plt.xlabel('Nombre d\'inscrits')
    plt.ylabel('Densité')
    plt.tight_layout()
    plt.savefig('src/images/hist_inscrits_kde.png', dpi=150)
    plt.show()
except Exception:
    pass
### 14 Diagrammes en barres MAthplotlib