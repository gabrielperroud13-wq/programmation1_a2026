# =============================================================
# Exercice 1 - Structure, variables et constantes (sections 2.1 a 2.3)
#
# Auteur : Gabriel Perroud
# Date   : 2026-08-26
# Sujet  : Exercice 1 du cours 02
#
# CONSIGNE : remplace chaque None par ta reponse.
#            Ne change PAS les noms de variables : les tests s'en servent.
#            Verifie ton travail avec :  python -m unittest test_exercice_1.py
# =============================================================


# -------------------------------------------------------------
# PARTIE A - Questions a choix multiple                (15 min)
# -------------------------------------------------------------
# Reponds avec la lettre de ton choix, entre guillemets.
# Exemple :  reponse_a1 = "B"

# A1) Combien d'INSTRUCTIONS contient ce code ?
#         x = 10; y = 20
#         print(x + y)
#     A) 1     B) 2     C) 3     D) 4
reponse_a1 = None

# A2) Pourquoi Print("Bonjour") ne fonctionne-t-il pas ?
#     A) La fonction print() n'existe pas en Python
#     B) Python est sensible a la casse
#     C) Il manque un point-virgule a la fin
#     D) La chaine de caracteres est mal fermee
<<<<<<< HEAD:Cours 02/Exercices/exercice_1.py
reponse_a2 = "B"
=======
reponse_a2 = None
>>>>>>> 7b78822b92246fd0f893f1e9b76f7e1a8c092784:Cours 02/Exercices/4 - Ateliers autocorrigés/exercice_1.py

# A3) Quel nom de VARIABLE respecte la convention PEP 8 ?
#     A) nbEtudiants     B) NbEtudiants     C) nb_etudiants     D) 2_etudiants
reponse_a3 = "C"

# A4) Quel nom convient a une CONSTANTE ?
#     A) taux_tps        B) TAUX_TPS        C) TauxTps          D) tauxTPS
reponse_a4 = "B"

# A5) Quel est le type de la valeur True ?
#     A) str             B) int             C) bool             D) float
reponse_a5 = "C"

# A6) Que retourne type(3.0) ?
#     A) <class 'int'>   B) <class 'float'> C) <class 'str'>    D) une erreur
reponse_a6 = "B"


# -------------------------------------------------------------
# PARTIE B - Declarer des constantes                   (10 min)
# -------------------------------------------------------------
# Declare les trois constantes ci-dessous en respectant la convention
# vue a la section 2.3 (SCREAMING_SNAKE_CASE) et le type demande.

# B1) Le nom de ton college, une chaine de caracteres (str).
#     Valeur exacte attendue : Cegep de Trois-Rivieres
NOM_CEGEP = str("Cegep de Trois-Rivieres")

# B2) Le nombre de credits du programme, un entier (int).
#     Valeur attendue : 90
NOMBRE_CREDITS_PROGRAMME = int(90)

# B3) Le cout d'un credit, un nombre a virgule (float).
#     Valeur attendue : 2.75
COUT_PAR_CREDIT = float(2.75)


# -------------------------------------------------------------
# PARTIE C - Declarer des variables et calculer         (20 min)
# -------------------------------------------------------------
# C1) Cree cinq variables decrivant un etudiant.
#     Les VALEURS sont libres (mets les tiennes!), mais le TYPE est impose.

prenom = str("Gabriel")            # str, au moins 2 caracteres
nom_famille = str("Perroud")       # str, au moins 2 caracteres
age = int(17)               # int, strictement positif
moyenne_generale = float(100)  # float, entre 0.0 et 100.0
est_inscrit = bool(True)       # bool (True ou False)

# C2) Construis le nom complet a l'aide d'un f-string : "prenom nom_famille"
#     (un seul espace entre les deux)
nom_complet = f"Gabriel Perroud"

# C3) Calcule le cout total du programme.
#     Utilise les CONSTANTES de la partie B, jamais leurs valeurs directement.
cout_total_programme = float(247.5)


# -------------------------------------------------------------
# PARTIE D - Afficher les resultats                    (15 min)
# -------------------------------------------------------------
# Complete les appels a print() ci-dessous.
# Chaque ligne affichee doit contenir la valeur demandee.

# D1) Affiche le nom du cegep, precede de "Cegep : "
print("Cegep :", NOM_CEGEP)

# D2) Affiche le nom complet de l'etudiant, precede de "Etudiant : "
#     Utilise un f-string.
print("Etudiant :", nom_complet)

# D3) Affiche le cout total du programme, precede de "Cout total : "
#     et suivi de " $"
print("Cout total :",cout_total_programme)

# D4) Affiche le TYPE de chacune des variables age, moyenne_generale
#     et est_inscrit, en utilisant la fonction native type().
print(type(age))
print(type(moyenne_generale))
print(type(est_inscrit))

