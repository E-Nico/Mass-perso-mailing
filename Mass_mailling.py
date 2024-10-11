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
import pandas as pd


# Création d'un parser avec une description plus détaillée
parser = argparse.ArgumentParser(description="Ce soft permet d'envoyer des mails personnalisés en masse. Pensez à bien formater votre CSV afin de ne pas avoir de problème.\nLe nom des colonnes du CSV doit être identiques aux variables dans le mail")


# Définition des arguments sans répétition des valeurs
parser.add_argument('-c', '--csv', help="fichier csv avec l'ensemble des informations nécessaires",metavar='', required=True)
#parser.add_argument('-id', '--identifiant', help="identifiant unique de l'application",metavar='', required=True)
#parser.add_argument('-a', '--appname', help="nom de l'application",metavar='', required=True)
#parser.add_argument('-ao', '--appofficier', help="prénom de l'application officier",metavar='', required=True)
#parser.add_argument('-m', '--mail', help="mail de l'application officier",metavar='', required=True)



# Récupération des arguments fournis
args = parser.parse_args()

def get_data_csv():
    df = pd.read_csv(args.csv)
    header = df.head(0)
    dictionnaire = df.to_dict()
    for head in header:
        print(dictionnaire[head][0])


def get_mail_template():
    print("Ok ça fonctionne !")

if __name__ == "__main__" :
    get_data_csv()