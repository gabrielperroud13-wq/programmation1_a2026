# valide = False
# while valide == False:
#     try:
#         age = int(input("Quel est ton âge "))
#         print("Vous avez", age, "ans")
#         a = 10 / 0
#         valide = True
#     except ValueError:
#         print("une erreur est survenue!")
#     except ZeroDivisionError:
#         print("une erreur est survenue!")
#     except:
#         print("une erreur est survenue!")

# print("Fin")


# reponses_valides = ("o", "n")

# reponse = input("Continuer ? (o/n) : ").strip().lower()
# while reponse not in reponses_valides:
#     print("Réponse invalide.")
#     reponse = input("Continuer ? (o/n) : ").strip().lower()