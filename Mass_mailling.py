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

from email.message import EmailMessage
import smtplib, ssl
import outlook
mail = outlook.Outlook()
#Features to add :
# - L'ajout du mode "confirmation"
# - Une description plus exhaustive de ce que fait l'application et comment l'utiliser

# Création d'un parser avec une description plus détaillée
parser = argparse.ArgumentParser(description="Ce soft permet d'envoyer des mails personnalisés en masse. Pensez à bien formater votre CSV afin de ne pas avoir de problème.\nLe nom des colonnes du CSV doit être identiques aux variables dans le mail")


# Définition des arguments sans répétition des valeurs
parser.add_argument('-c', '--csv', help="fichier csv avec l'ensemble des informations nécessaires",metavar='', required=True)
parser.add_argument('-t', '--template', help="template de mail au format texte avec les variables",metavar='', required=True)
parser.add_argument('-m', '--mode', help="deux modes sont disponibles, confirmé [0] ou non confirmé [1]. Dans le mode confirmé, chaque mail devra être validé dans le prompt avant envoie. Dans le mode non confirmé, les mails sont envoyés sans confirmation",metavar='', required=False)



# Récupération des arguments fournis
args = parser.parse_args()

def get_header_csv():
    df = pd.read_csv(args.csv)
    header = df.head(0)
    return header.columns

def get_dictionnaire_csv():
    df_dict = pd.read_csv(args.csv)
    dictionnaire = df_dict.to_dict()
    return dictionnaire


def get_mail_template():
    fichier = open(args.template, "r")
    tempmail = fichier.read()
    fichier.close()
    return tempmail

def create_perso_template(header, dictionnaire_data, tempmail):
    dict_var_header = []
    for value in header:
        dict_var_header.append(f'${value}$')
    print(dictionnaire_data[header[0]])  
    for i in range(0,len(dictionnaire_data[header[0]])):
        print(i)
        mail = tempmail

        for y in range (0,len(dictionnaire_data)):
            print(f'HEADER[Y] = {header[y]}')
            if f'${header[y]}$' in tempmail:
                print(f'${header[y]}$ est bien dans le template')
                print(f'header[y] = {header[y]}')
                print(f'str(dictionnaire_data[header[i]][i] = {str(dictionnaire_data[header[y]][i])}')
                mail = mail.replace(f'${header[y]}$',str(dictionnaire_data[header[y]][i]))
            else:
                print(f'${header[y]}$ nest pas dans le template')

            print("\n")
           
            
        print(mail)
        print("--------------------------------------------------------------------------")

def send_mail(template):
    sender = "nlefevre650@headmind.com"
    recipient = "nlefevre650@headmind.com"
    message = "Hello world!"

    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Test Email"
    email.set_content(message)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, "my_outlook_password_123")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()


if __name__ == "__main__" :
    #header = get_header_csv()
    #dictionnaire_data = get_dictionnaire_csv()
    #print(dictionnaire_data)
    #tempmail = get_mail_template()
    #create_perso_template(header, dictionnaire_data, tempmail)
    temp = "Bonjour $application officier$ Merci de mettre à jour l'application : ID : $ID$ NAME : $app name$ Cordialement,"
    send_mail(temp)

