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

## Performances sur une machine standard

**Configuration matérielle** :  
- 16 Go RAM  
- AMD Ryzen 7 7730U with Radeon Graphics – 16 CPU ~ 2 GHz  

**Temps d’exécution observé** :

| Nombre maximum | Temps d'exécution |
|----------------|-------------------|
| 10 000         | ~ 6 secondes      |
| 100 000        | ~ 15 minutes      |

Dès que l’on atteint 100 000, le temps de calcul devient rédhibitoire (15 minutes contre 6 secondes pour 10 000).  
**Ce constat justifie pleinement l’utilisation d’une approche HPC parallèle et distribuée.**


---
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
---

## Architecture du projet (à venir)

- Partitionnement de l’intervalle de recherche en sous‑domaines.
- Distribution sur plusieurs nœuds via MPI.
- Implémentation du crible d’Ératosthène avec PETSc (vecteurs distribués).
- Réduction et rassemblement des résultats.
- Analyse de speedup et d’efficacité.
