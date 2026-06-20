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
