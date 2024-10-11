#Entrée :
# - Fichier CSV avec les personnes à contacter.
# - Template de mail.
# - Les variables à modifier dans le mail.

#Sortie :
# - Affichage du mail à envoyer 
# - Affichage des mails envoyés

import csv
import os
import argparse


# Création d'un parser avec une description plus détaillée
parser = argparse.ArgumentParser(description='Description of your program')

# Définition des arguments sans répétition des valeurs
parser.add_argument('-id', '--identifiant', help="Identifiant unique de l'application",metavar='', required=True)
parser.add_argument('-a', '--appname', help="Nom de l'application",metavar='', required=True)
parser.add_argument('-ao', '--appofficier', help="Prénom de l'application officier",metavar='', required=True)
parser.add_argument('-m', '--mail', help="mail de l'application officier",metavar='', required=True)



# Récupération des arguments fournis
args = parser.parse_args()

def get_data_csv():
    print("")
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def get_mail_template():
    print("Ok ça fonctionne !")

if __name__ == "__main__" :
    get_mail_template()