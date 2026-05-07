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

![Photo1](Figure_1.png)
![Photo2](Figure_2.png)

**Temps d’exécution observé** :

| Nombre maximum | Temps d'exécution |
|----------------|-------------------|
| 10             | ~ 0.000008 s      |
| 100            | ~ 0.000172 s      |
| 1 000          | ~ 0.012303 s      |
| 10 000         | ~ 1.356 s         |
| 20 000         | ~ 5.6 s           |
| 30 000         | ~ 25 s            |
| 50 000         | ~ 51 s            |
| 100 000        | ~ 179 s           |

Dès que l’on atteint 100 000, le temps de calcul devient plus important. L'idéal est de pouvoir simuler pour des nombres vraiment grands.  
**Ce constat justifie pleinement l’utilisation d’une approche HPC parallèle et distribuée.**


---
```python
import numpy as np
import time
import matplotlib.pyplot as plt

debut = time.time()
#nombre_max = 50000
liste_temps =  [10, 100, 1000, 10000, 20000, 30000, 50000]

def diviseurs(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

liste_valeur = []
liste_nombre = []
for nombre_max in liste_temps:
    prime_list = []
    for k in range(2,nombre_max + 1):
        j = diviseurs(k)     
        if len(j) == 2:
            prime_list.append(k)
    end = time.time()
    temps = end - debut
    liste_valeur.append(temps)
    print(f"Les nombres premiers inférieurs ou égales à {nombre_max} sont: {prime_list}")       

    print(f"Il y a {len(prime_list)} nombres premiers inférieurs ou égales à {nombre_max}.\n")    
    liste_nombre.append(len(prime_list))
    print(f"Temps total: {temps}")

plt.figure(figsize=(8, 5))
plt.plot(liste_temps, liste_valeur, "b-", linewidth=2)
plt.xlabel("Nombre max")
plt.ylabel("Durée")
plt.legend()
plt.title("Durée par rapport au nombre_max")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(liste_temps, liste_nombre, "r-", linewidth=2)
plt.xlabel("Nombre_max")
plt.ylabel("Nombre de nombres premiers trouvés")
plt.legend()
plt.title("Nombre de nombre premiers avant Nombre_max")
plt.show()


```
---

## Architecture du projet (à venir)

- Partitionnement de l’intervalle de recherche en sous‑domaines.
- Distribution sur plusieurs nœuds via MPI.
- Implémentation du crible d’Ératosthène avec PETSc (vecteurs distribués).
- Réduction et rassemblement des résultats.
- Analyse de speedup et d’efficacité.
