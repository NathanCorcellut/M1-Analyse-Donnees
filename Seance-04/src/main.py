#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']


## 1 - VISUALISER DES DISTRIBUTIONS
## 1.A - Distributions statistiques de Variables DISCRETES

## Question 1.A.1 - Loi de Dirac
def distrib_dirac_discret(a, x_min, x_max):
    X = []
    P = []
    for i in range(x_min, x_max+1):
        X.append(i)
        if i == a:
            P.append(1.0)
        else :
            P.append(0.0)

    return X, P

# Paramètrage
a = 7
x_min = 0
x_max = 20

# On génère la distribution
X, P = distrib_dirac_discret(a, x_min, x_max)

# On visualise la distribution
plt.stem(X, P)
plt.title("Loi de Dirac centrée en a = {}".format(a))
plt.xlabel("x")
plt.ylabel("Pr(X = x)")
plt.ylim(0, 1.1)
plt.grid(True)
plt.savefig("./output/1_A_Distrib_Discretes/1_Dirac_discret.png")
plt.close()




## Question 1.A.2 - Loi Uniforme Discrète
def distrib_uniforme_discret(x_min, x_max):
    X = []
    P = []

    n = (x_max - x_min) + 1
    for i in range(x_min, x_max+1):
        X.append(i)
        P.append(1/n)

    return X, P

# Paramètrage
x_min = 1
x_max = 10

# On génère la distribution
X, P = distrib_uniforme_discret(x_min, x_max)

# On visualise la distribution
plt.stem(X, P)
plt.title("Loi uniforme discrète sur l'intervalle [[{} ; {}]]".format(x_min, x_max))
plt.xlabel("x")
plt.ylabel("Pr(X = x)")
plt.grid(True)
plt.savefig("./output/1_A_Distrib_Discretes/2_Uniforme_discret.png")
plt.close()




## Question 1.A.3 - Loi Binomiale

## Question 1.A.4 - Loi de Poisson

## Question 1.A.5 - Loi de Zipf-Mandelbrot


def zipf_mandelbrot(s, q, N):
    """
    Renvoie les valeurs x et les probabilités P(X=x) pour la loi de Zipf-Mandelbrot.
    """
    x = np.arange(1, N + 1)
    # calcul du dénominateur (constante de normalisation)
    normalization = np.sum(1.0 / (x + q)**s)
    p = 1.0 / (x + q)**s / normalization
    return x, p

# paramètres
s = 1.5
q = 2
N = 50

# génération
x, p = zipf_mandelbrot(s, q, N)

# visualisation
plt.figure(figsize=(8,4))
plt.stem(x, p)
plt.title("Loi de Zipf-Mandelbrot (s={}, q={}, N={})".format(s,q,N))
plt.xlabel("x")
plt.ylabel("P(X = x)")
plt.yscale("log")  # utile car la distribution est très heavy tail
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.savefig("./output/1_A_Distrib_Discretes/5_Zipf_Mandelbrot_discret.png")
plt.close()

## 1.B - Distributions statistiques de Variables CONTINUES
## Question 1.B.1 - Loi de Poisson

## Question 1.B.2 - Loi Normale

## Question 1.B.3 - Loi Log-normale

## Question 1.B.4 - Loi Uniforme

## Question 1.B.5 - Loi du Chi²

## Question 1.B.6 - Loi de Pareto



## 2 - CALCUL MOYENNE ET ECART-TYPE
# Définition des fonctions

# Test des fonctions