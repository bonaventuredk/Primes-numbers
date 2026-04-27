# Primes-numbers
Développement d'un moteur de calcul haute performance (HPC) dédié au dénombrement de nombres premiers sur des plages de données massives.

# Auteur
## Dohemeto Bonaventure K.

-Le projet transpose le crible d'Ératosthène en un environnement distribué en utilisant le framework PETSc et le protocole MPI.

-Points clés :

    Calcul Parallèle : Segmentation de l'espace de recherche via des vecteurs distribués (Vec MPI) pour lever les barrières de mémoire RAM.

    Optimisation HPC : Gestion fine de la localité du cache et réduction des coûts de communication inter-nœuds.

    Analyse de Scalabilité : Étude comparative des performances (Speedup) en fonction du nombre de processeurs.

    Outils : Python/C++, PETSc, MPI, Scibian.

# Introduction
Pour planter le décort, considérons juste un code tout simple permettant de lister les nombres premiers inférieurs ou égales à un nombre fixé. Nous fixerons ce nombre respectivement à 100, 1000, 10000 et 100000 pour nos simulations (de base). 

Voici le code : 

```python
import numpy as np

nombre_max = 100000

def diviseurs(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

prime_list = []
for k in range(2,nombre_max + 1):
    j = diviseurs(k)     
    if len(j) == 2:
        prime_list.append(k)
        

print(f"Les nombres premiers inférieurs ou égales à {nombre_max} sont: {prime_list}")       

print(f"Il y a {len(prime_list)} nombres premiers inférieurs ou égales à {nombre_max}.\n")    
```

Pour un pc avec les performances suivantes: 16Giga RAM, AMD Ryzen 7 7730U with RadeonGraphics - 16CPU ~ 2Ghz, on peut déjà constater qu'à partir de 100000, il prend énormément(comparé à des nombres plus petits) de temps juste pour finir les vérifications. En moyenne 15 min, comparé à 6 secondes quand on fixe 10000. 

CE QUI JUSTIFIE DONC L'UTILITé de cette approche.
