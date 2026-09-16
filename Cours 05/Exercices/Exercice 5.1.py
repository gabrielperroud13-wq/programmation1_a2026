compteur = 10
while compteur >= 0:
    print(compteur)
    compteur -= 1
print("Décolage")

# code_trouve = False
# while code_trouve == False:
#     code = int(input("Donne moi un code  : "))
#     if code == 8:
#         print("Trouvé")
#         code_trouve = True
#     else:
#         print("Bien essayé") 





while True:
    compteur = str(input("Donne moi un code  : "))
    if (compteur == "python123"):
        print("Accès Authorisé !")
        break
    else:
        print("Accès Refusé")
