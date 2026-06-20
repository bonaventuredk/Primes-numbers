import numpy as np
import time
import matplotlib.pyplot as plt
from numba import njit

@njit
def trouver_premiers_numba(n_max):
    """Retourne la liste des nombres premiers <= n_max (algorithme d'origine)"""
    premiers = []
    for n in range(2, n_max + 1):
        nb_div = 0
        for i in range(1, n + 1):
            if n % i == 0:
                nb_div += 1
        if nb_div == 2:          
            premiers.append(n)
    return premiers


liste_temps = [10, 100, 1000, 10000, 20000, 30000, 50000, 100000]

liste_valeur = []     # temps cumulés
liste_nombre = []     # nombres de premiers trouvés

# Appel "à vide" pour forcer la compilation Numba avant la première mesure
trouver_premiers_numba(10)

debut = time.time()  

for nombre_max in liste_temps:
    prime_list = trouver_premiers_numba(nombre_max)

    end = time.time()
    temps = end - debut
    liste_valeur.append(temps)

    print(f"Les nombres premiers inférieurs ou égales à {nombre_max} sont: {prime_list}")
    print(f"Il y a {len(prime_list)} nombres premiers inférieurs ou égales à {nombre_max}.\n")
    liste_nombre.append(len(prime_list))
    print(f"Temps cumulé: {temps:.3f} s")


plt.figure(figsize=(8, 5))
plt.plot(liste_temps, liste_valeur, "b-", linewidth=2)
plt.xlabel("Nombre max")
plt.ylabel("Durée cumulée (s)")
plt.legend(["Durée"])
plt.title("Durée par rapport au nombre_max (avec Numba)")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(liste_temps, liste_nombre, "r-", linewidth=2)
plt.xlabel("Nombre_max")
plt.ylabel("Nombre de nombres premiers trouvés")
plt.legend(["Quantité"])
plt.title("Nombre de nombres premiers avant Nombre_max")
plt.show()
