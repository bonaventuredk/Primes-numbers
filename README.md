# Primes-numbers
Développement d'un moteur de calcul haute performance (HPC) dédié au dénombrement de nombres premiers sur des plages de données massives.

# Auteur
##Dohemeto Bonaventure K.

-Le projet transpose le crible d'Ératosthène en un environnement distribué en utilisant le framework PETSc et le protocole MPI.

-Points clés :

    Calcul Parallèle : Segmentation de l'espace de recherche via des vecteurs distribués (Vec MPI) pour lever les barrières de mémoire RAM.

    Optimisation HPC : Gestion fine de la localité du cache et réduction des coûts de communication inter-nœuds.

    Analyse de Scalabilité : Étude comparative des performances (Speedup) en fonction du nombre de processeurs.

    Outils : Python/C++, PETSc, MPI, Scibian.

