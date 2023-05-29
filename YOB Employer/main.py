from DataBaseFunction import *
from GuiFunction import *
import sys
import random
import time
#Window Afficher Data Client

YobAdmistration=QtWidgets.QApplication(sys.argv)
windowTableClient=windowF(1370,700,'Info','..\\YOB Utilisateur\\YOB PROJECT\\png\\YOB.png','')
windowTableClient.move(0,0)
inputrecherchePersonne=inputF(20,20,300,40,'background-color:#dfdfdfdf;font-size:20px;',windowTableClient,'Enter ')
buttonRecherche=buttonF(340,20,150,40,'font-size:15px;',windowTableClient,'Search')
tableRecherche = QtWidgets.QTableWidget(windowTableClient)
tableRecherche.setGeometry(15, 100, 1365, 590)
tableRecherche.setColumnCount(13)
tableRecherche.setHorizontalHeaderLabels(('Id,Last name,First name,Age,Id card,Email,Phone number,City,Gender,Rib,Balance,Password,Date_Creation').split(','))
tableRecherche.horizontalHeader().setStyleSheet('::section{Background-color:black;color:white;}')
tableRecherche.verticalHeader().setStyleSheet('::section{Background-color:black;color:white;}')
labelDataVide = labelF(600, 340, 200, 50, 'font-size:25px;', windowTableClient, 'Nothing is found !!!')
labelDataVide.close()
tableRecherche.close()
table = QtWidgets.QTableWidget(windowTableClient)
table.setGeometry(10, 100, 1420, 590)
table.close()
def refrech():
    inputrecherchePersonne.setText('')
    tableRecherche.close()
    if nombreClientInDataBase() != 0:
        labelDataVide.close()
        sortBaseDonne()
        table.setRowCount(nombreClientInDataBase())
        table.setColumnCount(13)
        table.setHorizontalHeaderLabels(('Id,Last name,First name,Age,Id card,Email,Phone number,City,Gender,Rib,Balance,Password,Date_Creation').split(','))
        table.horizontalHeader().setStyleSheet('::section{Background-color:black;color:white;}')
        table.verticalHeader().setStyleSheet('::section{Background-color:black;color:white;}')
        for e in range(1, nombreClientInDataBase() + 1):
            x = returnDataApartirId(e)
            if x != None:
                for t in range(0, 13):
                    table.setItem(e - 1, t, QtWidgets.QTableWidgetItem(str(x[t])))
        table.show()
    else:
        labelDataVide.show()
refrech()
buttonRefreche=buttonF(1210,20,120,40,'font-size:18px;',windowTableClient,'refresh')
buttonAjouterClientTableW=buttonF(1050,20,150,40,'font-size:15px;',windowTableClient,'Add client')
buttonDeleteClientTableW=buttonF(880,20,150,40,'font-size:15px;',windowTableClient,'Delete client')
buttonInsertMoney=buttonF(720,20,150,40,'font-size:15px;',windowTableClient,'Transfer')
#Window ajouter Client
windowAjouterClient=windowF(400,700,'Add client :','..\\YOB Utilisateur\\YOB PROJECT\\png\\YOB.png','')
windowAjouterClient.move(400,0)
Ville_list=['Afourar','Agadir','Agdz','Agourai','Aguelmous','Ahfir','Ain Bni Mathar','Ain Aleuh','Ain Dorij','Ain Jemaa','Ait Benhaddou','Ain Defali','Ain El Aouda','Ain Erreggada','Ain Taoujdate','Ait Boubidmane','Ait Bouhlal','Ait Daoud','Ait laaza','Ait ishaQ','Ait Ourir','Aklim','Azrou','Ajdir','Al Aatoui','Al-Houceima','Amalou lghreben','Amgal','Amizmiz','Aoufous','Arbaoua','Arfoud','Asilah','Assahrij','Bab Berred','Bab Taza','Ben Ahmed','Beni Chiker','Beni Ansar','Bni mellal','Ben Slimane','ben Taieb','Ben Yakhlef','Berkane','Berrechid','Bhalil','Bir Ganbirdus','Bir Lehlou','Bni Bouayach','Bni Drar','Bni Hadifa','Beni Tadjit','Bouarfa','Bou Craa','Bouanane','Boudnib','Boufakrane','Bouguedra','Bouizakarne','Boujad','Boujdour','Bouknadel','Boulemane','Bouskoura','Bouznika','Bradia','Brikcha','Casablanca','Chefchaouen','Chemaia','Chichaoua','Dakhla','Driouch','Dar Gueddari','Dar Kebdani','Demnate','Douar Bel Aguide','Debdou','El Aioun Sidi Mellouk','El Guerdane','El Hajeb','El Hanchane','El jadida','El Menzel','El Ouatia','Erfoud','Errachidia','Essaouira','Fes','FnideQ','FQuih Ben Salah','Er-Rich','Guelmim','Goulmima','Guerguerate','Guisser','Guercif','Had Kourt','Hagunia','Haj Kaddour','Harhoura','Ighrem-Nougdale','Ihddaden','Ifrane','Imilchile','Imilili','Imintanoute','Inzegane','Issaguen','Itzer','Jerada','Jorf','Jorf El Melha','Jemaa Sahim','Kassita','Kattara','Kenitra','Kehf Nsour','Ketama','Khemis Dades','Khemisset','Khemis Sahel','Khemis Zemamra','Khenichet','Khenifra','Khouribga','Ksar El-Kbir','Klaat Magouna','Laayoune','Laguira','Lalla Mimouna','Larache','Lixus','Lqliaa','Madagh','Marrakech','Martil','Mechra Bel Ksiri','Mediak','Mediouna','Mehdia','Meknes','Melloussa','Midelt','Mirleft','Mohammedia','Moqrisset','Moulay Ali Cherif','Moulay Bousselham','Moulay Idriss Zerhoun',"M'rirt",'Nador','Nhima','Ouarzazate','Oualidia','Ouezzane','Oujda','Oukaimeden','Oulad Amrane','Oulade Ayade','Oualad Berhil','Oulad Frej','Oulade Ghedbane','Oulad H Riz Sahel',"Oulade M'Rah",'Oulade M Barek','Oulad Teima','Oulad Zbair','Oulade Tayteb','Oulad Youssef','Oulmes','Ounagha','Rabat','Rommani','Ras El Ain','Ras El Ma','Ribate El Kheir','Rissani','Sebaa Aiyoun','Safi','Saida','Sale','Sala El Jadida','Sebt El Maarif','Sebt Gzoula','Settat','Sefrou','Sid Zouin','Sidi Abdellah Ghiat','Sidi Addi','Sidi Allal Tazi','Sidi Bou Othmane','Sidi Boubker','Sidi Jaber','Sidi Kacem','Sidi Lyamani','Sidi Rahhal','Sidi Slimane','Sidi Smail','Sidi Taibi','Sidi Yahya El Gharb','Skhirat','Smara',"Souq Larbtetache'a al Gharb",'Taddert','Tafetachte','Tafarsit','Taghjijt','Tahala','Tahanout','Tainaste','Taliouine','Talmest','Talssint','Tanger','Tan-Tan','Tamallalt','Tamanar','Tameslouht','Tamesna','Taounate','Tarouddant','Tata','Taznakht','Telouet','Temara','Temsia','Tetouane','Tifariti','Tiflet','Tighza','Timahdite','Tinejdad','Tinghir','Tinmel','Tounfite','Tiznit','Tiztoutine','tifelt','Youssoufia','Zagora','Zaio','Zeghanghane','Zemamra','Zaouit Cheikh']
label1=labelF(130,20,200,40,'font-size:25px;',windowAjouterClient,'Add client  ')
label1.setAlignment(QtCore.Qt.AlignCenter)
labelProbleme=labelF(20,650,200,40,'font-size:15px;color:red;',windowAjouterClient,'<b><u>Problem !!!</u></b>')
labelProbleme.close()
labelNom=labelF(50,100,100,40,'font-size:15px;',windowAjouterClient,'Last name : ')
inputNom=inputF(150,100,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient,'Enter the last name : ')
labelPrenom=labelF(50,170,100,40,'font-size:15px;',windowAjouterClient,'First name : ')
inputPrenom=inputF(150,170,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient,'Enter the first name : ')
labelAge=labelF(50,230,100,40,'font-size:15px;',windowAjouterClient,'Age : ')
inputAge=comboBoxF(150,230,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient)
inputAge.addItem("Age")
for i in range(18, 110, 1):
    inputAge.addItem(str(i))
labelCin=labelF(50,290,100,40,'font-size:15px;',windowAjouterClient,'Id card : ')
inputCin=inputF(150,290,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient,'Enter the Id card : ')
labelEmail=labelF(50,350,100,40,'font-size:15px;',windowAjouterClient,'Email : ')
inputEmail=inputF(150,350,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient,'Enter the Email : ')
labelTele=labelF(50,410,100,40,'font-size:15px;',windowAjouterClient,'Phone number : ')
inputTele=inputF(150,410,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient,'Enter the phone number : ')
labelVille=labelF(50,470,100,40,'font-size:15px;',windowAjouterClient,'City : ')
inputVille=comboBoxF(150,470,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient)
inputVille.addItem("City")
for ville in Ville_list:
    inputVille.addItem(ville)
inputSex=comboBoxF(150,530,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient)
inputSex.addItem('Gender')
inputSex.addItem('Female')
inputSex.addItem('Male')
labelSexe=labelF(50,530,100,40,'font-size:15px;',windowAjouterClient,'Gender : ')
labelPassword=labelF(50,590,100,40,'font-size:15px;',windowAjouterClient,'Password : ')
inputPassword=inputF(150,590,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowAjouterClient,'Enter the password : ')
buttonAjouterClient=buttonF(190,640,100,40,'font-size:15px;',windowAjouterClient,'Add')
#Window delete client
windowDeleteClient=windowF(350,250,'Delete client :','..\\YOB Utilisateur\\YOB PROJECT\\png\\YOB.png','')
windowDeleteClient.move(900,100)
label2=labelF(120,20,200,40,'font-size:25px;',windowDeleteClient,'Delete client  ')
labelRibRecherche=labelF(50,100,100,40,'font-size:15px;',windowDeleteClient,'Rib : ')
inputRibRecheche=inputF(110,100,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowDeleteClient,'Enter the Rib  ')
buttonDeleteClient=buttonF(150,150,100,40,'font-size:15px;',windowDeleteClient,'Delete')
labelProblemeDeleteWindow=labelF(10,200,200,40,'color:red;font-size:15px;',windowDeleteClient,'')
labelProblemeDeleteWindow.close()
#Window insert money client
windowInsertMoneyClient=windowF(350,300,'Transfer :','..\\YOB Utilisateur\\YOB PROJECT\\png\\YOB.png','')
windowInsertMoneyClient.move(0,100)
label3=labelF(150,20,300,40,'font-size:25px;',windowInsertMoneyClient,'Transfer  ')
labelRib=labelF(50,100,100,40,'font-size:15px;',windowInsertMoneyClient,'Rib : ')
inputRib=inputF(110,100,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowInsertMoneyClient,'Enter the Rib  ')
labelMoney=labelF(50,150,100,40,'font-size:15px;',windowInsertMoneyClient,'Balance : ')
inputMoney=inputF(110,150,200,40,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',windowInsertMoneyClient,'Enter the balance  ')
buttonInsertMoneyClient=buttonF(150,200,100,40,'font-size:15px;',windowInsertMoneyClient,'Done ')
labelProblemeInsetWindow=labelF(10,250,300,40,'color:red;font-size:15px;',windowInsertMoneyClient,'')
labelProblemeInsetWindow.close()
#---------------
def rechercheRibB():
    table.close()
    if inputrecherchePersonne.text()!='':
        if len(recherche(inputrecherchePersonne.text()))!=0:
            tableRecherche.setRowCount(len(recherche(inputrecherchePersonne.text())))
            i=0
            for z in recherche(inputrecherchePersonne.text()):
                x = returnDataApartirId(z)
                for t in range(0, 13):
                    tableRecherche.setItem(i, t, QtWidgets.QTableWidgetItem(str(x[t])))
                i=i+1
            tableRecherche.show()
        else:
            labelDataVide.show()
    else:
        table.show()

def initialiserAjouteClient():
    inputPrenom.setText('')
    inputVille.setCurrentText('City')
    inputAge.setCurrentText('Age')
    inputSex.setCurrentText('Gender')
    inputTele.setText('')
    inputCin.setText('')
    inputEmail.setText('')
    inputPassword.setText('')
    inputNom.setText('')

def addClient():
    rib=str(random.randint(3000, 4000)) + str(random.randint(1000, 8000))
    if rechercheRib(rib)==0:
        rib = str(random.randint(3000, 4000)) + str(random.randint(1000, 8000))
    insert_personne(inputNom.text(), inputPrenom.text(), inputAge.currentText(), inputCin.text(), inputEmail.text(),inputTele.text(), inputVille.currentText(), inputSex.currentText(),rib, 0, inputPassword.text())
    initialiserAjouteClient()
    labelProbleme.setText('The add process is done successfully ')#
    labelProbleme.show()
def deleteClient():
    e=rechercheRib(inputRibRecheche.text())
    if e!=0:
        deleteDataClient(e)
        labelProblemeDeleteWindow.setText('Client is <u>deleted</u>')
    else:
        labelProblemeDeleteWindow.setText('No client is existed with this rib : '+str(inputRibRecheche.text()))
    inputRibRecheche.setText('')
    labelProblemeDeleteWindow.show()
def insertMony():
    if rechercheRib(inputRib.text())!=0:
        x=returnDataApartirId(rechercheRib(inputRib.text()))
        nvsolde=float(x[10])+float(inputMoney.text())
        cursor.execute("UPDATE client SET solde=%s WHERE idClient=%s", (nvsolde, x[0]))
        conn.commit()
        labelProblemeInsetWindow.setText('The transfer process is done successfully ')
    else:
        labelProblemeInsetWindow.setText('No client is existed with this rib : '+str(inputRib.text()))
    labelProblemeInsetWindow.show()
def tableClient_AjouterClient():
    windowAjouterClient.show()
def tableClient_DeleteClient():
    windowDeleteClient.show()
def tableClient_InsertMoney():
    windowInsertMoneyClient.show()
buttonRecherche.clicked.connect(rechercheRibB)
buttonInsertMoneyClient.clicked.connect(insertMony)
buttonInsertMoney.clicked.connect(tableClient_InsertMoney)
buttonDeleteClient.clicked.connect(deleteClient)
buttonAjouterClientTableW.clicked.connect(tableClient_AjouterClient)
buttonAjouterClient.clicked.connect(addClient)
buttonRefreche.clicked.connect(refrech)
buttonDeleteClientTableW.clicked.connect(tableClient_DeleteClient)
windowTableClient.show()


YobAdmistration.exec_()
