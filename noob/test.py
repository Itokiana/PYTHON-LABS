# def main():
#     # recolter une valeur porte monnaie
#     wallet = 125
#     # creer un produit qui aura pour valeur 50
#     product = 50
#     # afficher la nouvelle valeur du porte monnaie, apres son achat
#     print("Le reste de votre porte monnaie est de: " + str(wallet - product))
#
#
# if __name__ == '__main__':
#     main()

# age = input("Quel est votre age? \n")
#
# import pickle
#
# with open("test", "r") as my_file:
#     content = my_file.read()
#     print(content)

# score = {
#     "j1": 20,
#     "j2": 10,
#     "j3": 1
# }
#
# with open("data.json", "wb") as data:
#     my_pickler = pickle.Pickler(data)
#     my_pickler.dump(score)

from tools.Personne import *

p = Personne()
print(p.nom)