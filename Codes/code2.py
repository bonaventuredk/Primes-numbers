from mpi4py import MPI
import math
import time
import sys

def petits_premiers(limit):
    """Retourne la liste des nombres premiers <= limit (crible simple)."""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:limit+1:step] = [False] * ((limit - start)//step + 1)
    return [i for i, is_p in enumerate(sieve) if is_p]

def crible_segmente(debut, fin, petits):
    """Crible sur [debut, fin] (inclus) avec la liste des petits premiers."""
    taille = fin - debut + 1
    est_premier = [True] * taille
    for p in petits:
        # Premier multiple de p dans l'intervalle
        start = max(p * p, ((debut + p - 1) // p) * p)
        for multiple in range(start, fin + 1, p):
            est_premier[multiple - debut] = False
    return [debut + i for i, flag in enumerate(est_premier) if flag]

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    N = 1_000_000
    if len(sys.argv) > 1:
        N = int(sys.argv[1])

    # --- Partitionnement ---
    total = N - 1
    base = total // size
    reste = total % size

    if rank < reste:
        debut = 2 + rank * (base + 1)
        fin = debut + base
    else:
        debut = 2 + rank * base + reste
        fin = debut + base - 1

    # --- Petits premiers (communs à tous) ---
    rootN = int(math.isqrt(N))
    petits = petits_premiers(rootN)

    # --- Calcul local ---
    start_time = time.time()
    premiers_locaux = crible_segmente(debut, fin, petits)
    end_time = time.time()
    temps_local = end_time - start_time

    # --- Rassemblement des résultats ---
    tous_les_premiers = comm.gather(premiers_locaux, root=0)
    temps_max = comm.reduce(temps_local, op=MPI.MAX, root=0)

    if rank == 0:
        resultat = []
        for bloc in tous_les_premiers:
            resultat.extend(bloc)
        print(f"N = {N} : {len(resultat)} nombres premiers")
        print(f"Temps maximal sur un processus : {temps_max:.3f} s")
        if len(resultat) >= 10:
            print("Derniers premiers :", resultat[-10:])

if __name__ == "__main__":
    main()
    