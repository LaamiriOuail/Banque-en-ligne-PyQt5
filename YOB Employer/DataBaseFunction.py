import random

import mysql.connector
import datetime
from PyQt5 import *
#Create Data Base
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='yob'
)
cursor=conn.cursor()

#Create Table
cursor.execute("""CREATE TABLE IF NOT EXISTS Client(
idClient int(5) NOT NULL AUTO_INCREMENT,
nom varchar(50) DEFAULT NULL,
prenom varchar(50) DEFAULT NULL,
age INTEGER DEFAULT NULL,
cin varchar(15) DEFAULT NULL,
emailAdress TEXT DEFAULT NULL,
Telephone TEXT DEFAULT NULL,
ville TEXT DEFAULT NULL,
sexe TEXT DEFAULT NULL,
rib TEXT DEFAULT NULL,
solde TEXT DEFAULT NULL,
password TEXT DEFAULT NULL,
date_Creation TEXT DEFAULT NULL,
historique1 Text DEFAULT NULL,
historique2 Text DEFAULT NULL,
historique3 Text DEFAULT NULL,
historique4 Text DEFAULT NULL,
historique5 Text DEFAULT NULL,
PRIMARY KEY(idClient)
)
""")
#Sorte data Base
def sortBaseDonne():
    cursor.execute("SELECT idClient,nom,prenom,age,cin,emailAdress,telephone,ville,sexe,rib,solde,password,date_Creation FROM client")
    resultats = cursor.fetchall()
    i = 1
    for x in resultats:
        cursor.execute("UPDATE client SET idClient=%s WHERE idClient=%s", (i, x[0]))
        i = i + 1
    conn.commit()
#Insert DATA IN Client Table
def insert_personne(nom,prenom,age,cin,emailAdress,Telephone,ville,sexe,rib,solde,password):
    query="""INSERT INTO Client(nom,prenom,age,cin,emailAdress,telephone,ville,sexe,rib,solde,password,date_Creation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    args=(nom,prenom,age,cin,emailAdress,Telephone,ville,sexe,rib,solde,password,datetime.date.today())
    try:
        cursor.execute(query,args)
        sortBaseDonne()
        conn.commit()
    except mysql.connector.Error as Errormsg:
        print(Errormsg)
#Fonction qui retourne idClient de personne logine
def loginDatabaseClient(Email,Password):
    cursor.execute("SELECT emailAdress,password FROM client")
    i=0
    resultats = cursor.fetchall()
    for x in resultats:
        #global i
        if (x[0],x[1])==(Email,Password):
            i=x[0]
            break
    return i
#Supprimer un Client
def deleteDataClient(id):
    cursor.execute("DELETE FROM client WHERE idClient="+str(id))
    sortBaseDonne()
    conn.commit()
#Changer le numeroTelephone
def changeInformation(idClient,nvNumeroTelephone,nvPassword):
    if nvPassword=='':
        cursor.execute("UPDATE client SET telephone=%s WHERE idClient=%s",(nvNumeroTelephone,idClient))
    if nvNumeroTelephone=='':
        cursor.execute("UPDATE client SET password=%s WHERE idClient=%s", (nvPassword, idClient))
    conn.commit()
#return data from id
def returnDataApartirId(id):
    cursor.execute("SELECT idClient,nom,prenom,age,cin,emailAdress,telephone,ville,sexe,rib,solde,password,date_Creation,historique1,historique2,historique3,historique4,historique5 FROM client WHERE idClient=%s",(id,))
    resultats=cursor.fetchall()
    for x in resultats:
        return x
#Email Existe ?
def emailExeste(email):
    cursor.execute( "SELECT idClient,emailAdress FROM client")
    i = 0
    resultats = cursor.fetchall()
    for x in resultats:
        if x[1] ==email:
            i = x[0]
            break
    #i=0 email n'existe pas : i=id Email Existe
    return i
def nombreClientInDataBase():
    cursor.execute("SELECT idClient FROM client")
    i = 0
    resultats = cursor.fetchall()
    for x in resultats:
        i=i+1
    #i=0 data n'existe pas : i=nombre d'element in data =>Data non vide
    return i
def SetHistorique(id,historique):
    cursor.execute("SELECT historique1,historique2,historique3,historique4,historique5 FROM client WHERE idClient=%s",(id,))
    resultats = cursor.fetchone()
    for x in resultats:
        if x[0]!='':
            if x[1]!='':
                if x[2]!='':
                    if x[3]!='':
                        if x[4]!='':
                            cursor.execute("UPDATE client SET historique1=%s WHERE id=%s", (x[1], id))
                            cursor.execute("UPDATE client SET historique2=%s WHERE id=%s", (x[2], id))
                            cursor.execute("UPDATE client SET historique3=%s WHERE id=%s", (x[3], id))
                            cursor.execute("UPDATE client SET historique4=%s WHERE id=%s", (x[4], id))
                            cursor.execute("UPDATE client SET historique5=%s WHERE id=%s", (historique, id))
                        else:
                            cursor.execute("UPDATE client SET historique5=%s WHERE id=%s", (historique, id))
                    else:
                        cursor.execute("UPDATE client SET historique4=%s WHERE id=%s", (historique, id))
                else:
                    cursor.execute("UPDATE client SET historique3=%s WHERE id=%s", (historique, id))
            else:
                cursor.execute("UPDATE client SET historique2=%s WHERE id=%s", (historique, id))
        else :
            cursor.execute("UPDATE client SET historique1=%s WHERE id=%s", (historique, id))
    conn.commit()
def nombreHistorique(id):
    cursor.execute("SELECT historique1,historique2,historique3,historique4,historique5 FROM client WHERE idClient=%s",(id,))
    resultats = cursor.fetchone()
    for x in resultats:
        if x[0]=='':
            return 0
        else:
            if x[1]=='':
                return 1
            else:
                if x[2]=='':
                    return 2
                else:
                    if x[3]=='':
                        return 3
                    else:
                        if x[4]=='':
                            return 4
                        else:
                            return 5
def rechercheRib(rib):
    cursor.execute("SELECT idClient,rib FROM client")
    i = 0
    resultats = cursor.fetchall()
    for x in resultats:
        if x[1]==rib:
            i=x[0]
            break
    return i
def recherche(index):
    cursor.execute("SELECT idClient,nom,prenom,age,cin,emailAdress,telephone,ville,sexe,rib,solde,password,date_Creation FROM client")
    y=list()
    resultats = cursor.fetchall()
    for x in resultats:
        for j in range(0,13):
            if str(x[j])==index:
                y.append(x[0])
                break
    return y
#print(returnDataApartirId(2))
#conn.close()
