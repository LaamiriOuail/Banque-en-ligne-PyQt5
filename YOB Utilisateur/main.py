import random
import secrets
import smtplib
import ssl
import string
import sys
import urllib.request
from email.message import EmailMessage
from PyQt5 import QtWidgets, QtGui, QtCore
from GuiFunction import *
from Class import *
from dataBase import *
#------------------------------------
YOB=QtWidgets.QApplication(sys.argv)
#Cree un class
client=Client('','','','','','','','','','','','','')
clientATransere=Client('','','','','','','','','','','','','')
#------------
# Problem window
ProblemConnetion=windowF(440,150,'ERROR','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\probleme\\probleme.jpeg')
labelProblem1=labelF(40, 10,240, 120,'font-size:19px;color:red;',ProblemConnetion,'<u><b>Problem</b></u>')
labelProblem=labelF(40, 30,340, 120,'font-size:16px;color:black;',ProblemConnetion,'')
buttonProblem=buttonF(390, 130,50, 20,'background-color:white;color:black;',ProblemConnetion,"OK")
buttonProblem.clicked.connect(ProblemConnetion.close)
#Logine Window
logineWindow=windowF(974,615,'Login','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\login\\login.png')
labelIdentifiant=labelF(625, 182,250,20,'color:white;font-size:14px;',logineWindow,"Enter your email :")
inputIdentifiant=inputF(620, 200,250, 40,'background-color:white;color:black;border-radius:15px;font-size:18px;',logineWindow,"Enter your email  ")
labelPassword=labelF(625, 242,250,20,'color:white;font-size:14px;',logineWindow,"Enter your password :")
inputPassword=inputF(620, 260,250, 40,'background-color:white;color:black;border-radius:15px;font-size:18px;',logineWindow,"Enter your password ")
inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
loginButton=buttonF(630, 310,100, 30,"font-size:18px;background-color:#cd5b51;color:white;border-radius:15px;border:1px ;",logineWindow,"Login")
signupButton=buttonF(755, 310,100, 30,"font-size:18px;background-color:#1b2e35;color:white;border-radius:15px;border:1px ;",logineWindow,"Sign up")
forgortpassword=buttonF(640,350,200,30,"background-color:#ddccba;border-radius:10px;",logineWindow,"I forgot the password ?")


# sing up window
Ville_list=['Afourar','Agadir','Agdz','Agourai','Aguelmous','Ahfir','Ain Bni Mathar','Ain Aleuh','Ain Dorij','Ain Jemaa','Ait Benhaddou','Ain Defali','Ain El Aouda','Ain Erreggada','Ain Taoujdate','Ait Boubidmane','Ait Bouhlal','Ait Daoud','Ait laaza','Ait ishaQ','Ait Ourir','Aklim','Azrou','Ajdir','Al Aatoui','Al-Houceima','Amalou lghreben','Amgal','Amizmiz','Aoufous','Arbaoua','Arfoud','Asilah','Assahrij','Bab Berred','Bab Taza','Ben Ahmed','Beni Chiker','Beni Ansar','Bni mellal','Ben Slimane','ben Taieb','Ben Yakhlef','Berkane','Berrechid','Bhalil','Bir Ganbirdus','Bir Lehlou','Bni Bouayach','Bni Drar','Bni Hadifa','Beni Tadjit','Bouarfa','Bou Craa','Bouanane','Boudnib','Boufakrane','Bouguedra','Bouizakarne','Boujad','Boujdour','Bouknadel','Boulemane','Bouskoura','Bouznika','Bradia','Brikcha','Casablanca','Chefchaouen','Chemaia','Chichaoua','Dakhla','Driouch','Dar Gueddari','Dar Kebdani','Demnate','Douar Bel Aguide','Debdou','El Aioun Sidi Mellouk','El Guerdane','El Hajeb','El Hanchane','El jadida','El Menzel','El Ouatia','Erfoud','Errachidia','Essaouira','Fes','FnideQ','FQuih Ben Salah','Er-Rich','Guelmim','Goulmima','Guerguerate','Guisser','Guercif','Had Kourt','Hagunia','Haj Kaddour','Harhoura','Ighrem-Nougdale','Ihddaden','Ifrane','Imilchile','Imilili','Imintanoute','Inzegane','Issaguen','Itzer','Jerada','Jorf','Jorf El Melha','Jemaa Sahim','Kassita','Kattara','Kenitra','Kehf Nsour','Ketama','Khemis Dades','Khemisset','Khemis Sahel','Khemis Zemamra','Khenichet','Khenifra','Khouribga','Ksar El-Kbir','Klaat Magouna','Laayoune','Laguira','Lalla Mimouna','Larache','Lixus','Lqliaa','Madagh','Marrakech','Martil','Mechra Bel Ksiri','Mediak','Mediouna','Mehdia','Meknes','Melloussa','Midelt','Mirleft','Mohammedia','Moqrisset','Moulay Ali Cherif','Moulay Bousselham','Moulay Idriss Zerhoun',"M'rirt",'Nador','Nhima','Ouarzazate','Oualidia','Ouezzane','Oujda','Oukaimeden','Oulad Amrane','Oulade Ayade','Oualad Berhil','Oulad Frej','Oulade Ghedbane','Oulad H Riz Sahel',"Oulade M'Rah",'Oulade M Barek','Oulad Teima','Oulad Zbair','Oulade Tayteb','Oulad Youssef','Oulmes','Ounagha','Rabat','Rommani','Ras El Ain','Ras El Ma','Ribate El Kheir','Rissani','Sebaa Aiyoun','Safi','Saida','Sale','Sala El Jadida','Sebt El Maarif','Sebt Gzoula','Settat','Sefrou','Sid Zouin','Sidi Abdellah Ghiat','Sidi Addi','Sidi Allal Tazi','Sidi Bou Othmane','Sidi Boubker','Sidi Jaber','Sidi Kacem','Sidi Lyamani','Sidi Rahhal','Sidi Slimane','Sidi Smail','Sidi Taibi','Sidi Yahya El Gharb','Skhirat','Smara',"Souq Larbtetache'a al Gharb",'Taddert','Tafetachte','Tafarsit','Taghjijt','Tahala','Tahanout','Tainaste','Taliouine','Talmest','Talssint','Tanger','Tan-Tan','Tamallalt','Tamanar','Tameslouht','Tamesna','Taounate','Tarouddant','Tata','Taznakht','Telouet','Temara','Temsia','Tetouane','Tifariti','Tiflet','Tighza','Timahdite','Tinejdad','Tinghir','Tinmel','Tounfite','Tiznit','Tiztoutine','tifelt','Youssoufia','Zagora','Zaio','Zeghanghane','Zemamra','Zaouit Cheikh']
singupWindow=windowF(974,615,'Signing up','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
labelBienvenue=labelF(500,90,400,50,'font-size:40px;color:blue;',singupWindow,"<i>Welcome to <b>YOB</b> </i>")
etoileFirstName=labelF(390, 210,160, 15,"color:red;font-size:15px;",singupWindow,"  *")
etoileFirstName.close()
labelFirstName=labelF(309, 210,160, 15,'font-size:15px;',singupWindow,'First name :')
inputFirstName=inputF(300, 230,160, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow,"First name")
etoileLastName=labelF(610, 210,160, 15,'font-size:15px;color:red;',singupWindow,'  *')
etoileLastName.close()
labelLastName=labelF(529, 210,160, 15,'font-size:15px;',singupWindow,'Last name :')
inputLastName=inputF(520, 230,160, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow,"Last name")
etoileSex=labelF(860, 210,160, 15,'font-size:15px;color:red;',singupWindow,'  *')
etoileSex.close()
labelSex=labelF(779, 210,160, 15,'font-size:15px;',singupWindow,'Gender :')
inputSex=comboBoxF(770, 230,140, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow)
inputSex.addItem('Gender')
inputSex.addItem('Female')
inputSex.addItem('Male')
etoileAge=labelF(395, 300,160, 20,'font-size:15px;color:red;',singupWindow,'*')
etoileAge.close()
labelAge=labelF(314, 300,160, 20,'font-size:15px;',singupWindow,'Age :')
inputAge=comboBoxF(300, 320,120, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow)
inputAge.addItem("Age")
for i in range(18, 110, 1):
    inputAge.addItem(str(i))
etoilePhoneNumber=labelF(600,300,160, 15,'font-size:15px;color:red;',singupWindow,'        *')
etoilePhoneNumber.close()
labelPhoneNumber=labelF(520,300,160, 15,'font-size:15px;',singupWindow,'Phone number :')
inputNumberPhone=inputF(520, 320,160, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow,"Phone number")
etoileAdressEmail=labelF(805, 300,160, 15,'font-size:15px;color:red;',singupWindow,'        *')
etoileAdressEmail.close()
labelAddress=labelF(725, 300,160, 15,'font-size:15px;',singupWindow,'Email address :')
inputAddress=inputF(715, 320,245, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow,"Email Adress")
etoileVille=labelF(450, 390,170, 20,'font-size:15px;color:red;',singupWindow,'*')
etoileVille.close()
labelVille=labelF(370, 390,170, 20,'font-size:15px;',singupWindow,'City :')
inputVille=comboBoxF(360, 410,180, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow)
inputVille.addItem("City")
for ville in Ville_list:
    inputVille.addItem(ville)
etoileCin=labelF(730, 390,170, 20,'font-size:15px;color:red;',singupWindow,'  *')
etoileCin.close()
labelCIN=labelF(650, 390,170, 20,'font-size:15px;',singupWindow,'Id card :')
inputCIN=inputF(640, 410,180, 36,'background-color:#dfdfdf;color:black;border-radius:15px;font-size:20px;',singupWindow,"Id card")
retourButton=buttonF(270,12 ,90, 35,'font-size:15px;background-color:#0479f7;border:2px solid white;border-radius:15px;color:white;',singupWindow,"Back")
signUpNow=buttonF(550, 500,160, 50,"background-color:#1b2e35;color:white;border-radius:25px;border:2px solid white;font-size:15px;",singupWindow,"Sign up ")


# Verifiet Email window
verWindow=windowF(974,615,'Signing up','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
verifietCodeEmailLabel=labelF(505,198,200, 50,'font-size:17px;',verWindow,"Code sent to your email : "+inputAddress.text())
inputverifietCodeEmail=inputF(510, 250,200, 50,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#dfdfdf;',verWindow,"Code")
buttonVerefietCode=buttonF(548,310,139,30,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#cd5b51;color:white;',verWindow,"Next")
retourButton1=buttonF(270, 12,90, 40,'font-size:15px;background-color:#0479f7;border:2px solid white;border-radius:15px;color:white;',verWindow,"Back")



# Password window
passwordWindow=windowF(974,615,'Sign up','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
labelEmailIdentifiante=labelF(460,150,500,50,'font-size:25px;',passwordWindow,"<u><b>Try to enter a complicated password</b></u>")
labelInputCodeIdentification=labelF(290,220,190,50,'font-size:20px;',passwordWindow,"Password : ")
etoilelabelInputCodeIdentification=labelF(400,220,20,50,'font-size:15px;color:red;',passwordWindow,'*')
etoilelabelInputCodeIdentification.close()
inputCodeIdentification=inputF(450,220,500,50,'border-radius:10px;border:2px solid #dfdfdf;font-size:28px;background-color:#dfdfdf;',passwordWindow,"Password")
labelInputVerCodeIdentification=labelF(290,300,190,50,'font-size:20px;',passwordWindow,"Password : ")
etoilelabelInputVerCodeIdentification=labelF(400,300,20,50,'font-size:15px;color:red;',passwordWindow,'*')
etoilelabelInputVerCodeIdentification.close()
inputVerCodeIdentification=inputF(450,300,500,50,'border-radius:10px;border:2px solid #dfdfdf;font-size:28px;background-color:#dfdfdf;',passwordWindow,"Password confirmation")
inputVerCodeIdentification.setEchoMode(QtWidgets.QLineEdit.Password)
buttonCreatCompte=buttonF(595,380,190,50,'border-radius:10px;border:2px solid white;font-size:20px;background-color:#cd5b51;',passwordWindow,"Create an account ")
retourButtonlogin=buttonF(270,12,90,40,'font-size:15px;background-color:#0479f7;border:2px solid white;border-radius:15px;color:white;',passwordWindow,"Back")



#home window
homewindow=windowF(674,615,'Home','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\homeWindow\\BackgroundHomewindow.jpg')
homewindow.setStyleSheet('background-color:#4f23434;')
buttonHistorique=buttonF(190,-4,140,50,'border-radius:15px;background-color:#4996ff;font-size:20px;color:white;',homewindow,'History')
buttonHistorique.setIcon(QtGui.QIcon('YOB PROJECT\png\\historik.png'))
buttonHome=buttonF(30,-4,140,50,'border-radius:15px;background-color:#4996ff;font-size:20px;color:white;',homewindow,'Home')
buttonHome.setIcon(QtGui.QIcon('YOB PROJECT\png\\home.png'))
comboParametre=comboBoxF(404,-4,240,50,'border-radius:15px;background-color:#4996ff;font-size:20px;color:white;',homewindow)
comboParametre.addItem('Setting')
comboParametre.addItem('Personal information')#Ok
comboParametre.addItem('Edit phone number')#Ok
comboParametre.addItem('Edit Password')#ok
comboParametre.addItem('Transfer')#Ok

#Window Transfer
transferWindow=windowF(974,615,'Transfer','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
labeltransfer=labelF(270,50,700,50,'background-color:#eeeeee;color:#3d85c6;font-size:45px;',transferWindow,'Transfer ')
labeltransfer.setAlignment(QtCore.Qt.AlignCenter)
labelRib=labelF(310,170,150,50,'font-size:25px;',transferWindow,'Rib : ')
inputRib=inputF(410,170,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',transferWindow,"Enter the client's Rib  ")
labelSendMoney=labelF(310,230,150,50,'font-size:25px;',transferWindow,'Balance : ')
inputSendMoney=inputF(410,230,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',transferWindow,'Entrer the amount')
sendButton=buttonF(550,300,130,40,"background-color:#bcbcbc;color:#3d85c6;font-size:20px;border-radius:15px;",transferWindow,"Send")
retourButtonTransferHome=buttonF(270,0,90,30,'font-size:15px;background-color:#0479f7;border-radius:15px;color:white;',transferWindow,"Home")


#Window Edit Password
editePasswordWindow=windowF(974,615,'Changing password...','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\Window Securite\\PasswordChenge.jpg')
labelLastPassword=labelF(310,170,150,50,'font-size:20px;color:white;',editePasswordWindow,'Old password : ')
inputLastPassword=inputF(510,170,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',editePasswordWindow,'Enter the old password')
labelNvPassword=labelF(310,230,150,50,'font-size:20px;color:white;',editePasswordWindow,'New Password : ')
inputNvPassword=inputF(510,230,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',editePasswordWindow,'Enter the new password')
labelNvPassword2=labelF(310,290,150,50,'font-size:20px;color:white;',editePasswordWindow,'New Password : ')
inputNvPassword2=inputF(510,290,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',editePasswordWindow,'Password confirmation')
inputNvPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
ChangeButton=buttonF(640,370,130,40,"background-color:#56c2dd;color:black;font-size:20px;border-radius:15px;",editePasswordWindow,"Confirm")
forgortpasswd=buttonF(610,450,200,30,"background-color:#ddccba;border-radius:10px;",editePasswordWindow,"I forgot the old password ?")
retourButtonEditepasswdHome=buttonF(10,10,90,30,'font-size:15px;background-color:#d2fafc;border-radius:15px;color:black;',editePasswordWindow,"Home")


#forgortpassworw windiw
foegortWindow=windowF(974,615,'Verification','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
labelfoegortWindow=labelF(505,198,200, 50,'font-size:17px;',foegortWindow,"Code sent to :"+client.getEmailAdress())
inputveriCodeEmail=inputF(510, 250,200, 50,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#dfdfdf;',foegortWindow,"Code")
buttonfoegortWindow=buttonF(548,310,139,30,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#cd5b51;color:white;',foegortWindow,"Next")
retourButtonFoegort_editepasswd=buttonF(270, 12,90, 40,'font-size:15px;background-color:#cd5b51;border-radius:15px;color:white;',foegortWindow,"Back")

#Window Edit Password Apres verifiete email
editePasswordWindowVerifietEmail=windowF(974,615,'Changing password...','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\Window Securite\\PasswordChenge.jpg')
labelNvPasswordVerifietCodeEmail=labelF(310,230,150,50,'font-size:20px;color:white;',editePasswordWindowVerifietEmail,'New Password : ')
inputNvPasswordVerifietCodeEmail=inputF(510,230,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',editePasswordWindowVerifietEmail,'Enter the new password')
labelNvPassword2VerifietCodeEmail=labelF(310,290,150,50,'font-size:20px;color:white;',editePasswordWindowVerifietEmail,'New Password : ')
inputNvPassword2VerifietCodeEmail=inputF(510,290,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',editePasswordWindowVerifietEmail,'Password confirmation')
ChangeButtonVerifietCodeEmail=buttonF(640,370,130,40,"background-color:#56c2dd;color:black;font-size:20px;border-radius:15px;",editePasswordWindowVerifietEmail,"Confirm")
retourButtonEditePasswordWindowVerifietEmail_Home=buttonF(10,10,90,30,'font-size:15px;background-color:#d2fafc;border-radius:15px;color:black;',editePasswordWindowVerifietEmail,"Back")


#Window Edit Phone number
editePhoneNumberWindow=windowF(974,615,'Changing phone number...','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\Window Securite\\phoneNumberWindow.jpg')
labelNvPhoneNumber=labelF(320,200,300,50,'font-size:20px;color:#643e94;',editePhoneNumberWindow,'New phone number : ')
inputNvPhoneNumber=inputF(310,250,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',editePhoneNumberWindow,'Enter the new phone number')
buttonchangePhoneWindow=buttonF(440,330,139,30,"background-color:#56c2dd;color:#643e94;font-size:20px;border-radius:15px;",editePhoneNumberWindow,"Confirm")
retourButtoneditePhonenumberWindowHomewindow=buttonF(10,12,90,30,'font-size:15px;background-color:#643e94;border-radius:15px;color:white;',editePhoneNumberWindow,"Home")


#information Window
informationPersonnel=windowF(974,615,'Personal information','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
Nom00=labelF(300,110,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  Last name : ")
Nom=labelF(420,110,200,50,"color:black;font-size:20px;",informationPersonnel,'')
Prenom00=labelF(300,170,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel," First name :")
Prenom=labelF(420,170,200,50,"color:black;font-size:20px;",informationPersonnel,'')
Age00=labelF(300,230,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  Age : ")
Age=labelF(390,230,200,50,"color:black;font-size:20px;",informationPersonnel,'')
Rib00=labelF(300,290,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  Rib : ")
Rib=labelF(390,290,200,50,"color:black;font-size:20px;",informationPersonnel,'')
Solde00=labelF(300,350,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  Balance : ")
Solde=labelF(410,350,200,50,"color:black;font-size:20px;",informationPersonnel,'')
CIN00=labelF(630,110,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  Id card : ")
CIN=labelF(720,110,200,50,"color:black;font-size:20px;",informationPersonnel,'')
Email00=labelF(630,170,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel," Email :")
Email=labelF(720,170,200,50,"color:black;font-size:17px;",informationPersonnel,'')
Ville00=labelF(630,230,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  City : ")
Ville=labelF(720,230,200,50,"color:black;font-size:20px;",informationPersonnel,"       "+'')
Phonenumber00=labelF(630,290,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"Phone number : ")
Phonenumber=labelF(780,290,200,50,"color:black;font-size:20px;",informationPersonnel,'')
Sexe00=labelF(630,350,300,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"  Gender : ")
Sexe=labelF(740,350,200,50,"color:black;font-size:20px;",informationPersonnel,'')
DateCreation00=labelF(450,410,350,50,"background-color:#4996ff;color:white;font-size:20px;border-radius:10px;",informationPersonnel,"Account creation in : ")
DateCreation=labelF(640,410,200,50,"color:black;font-size:20px;",informationPersonnel,'')
buttonTelechargerPdf=buttonF(500,500,250,50,"background-color:#bcbcbc;color:#3d85c6;font-size:20px;border-radius:15px;",informationPersonnel,"Download pdf")
labelinformationPersonnel=labelF(270,35,700,50,'background-color:#eeeeee;color:#3d85c6;font-size:25px;',informationPersonnel,'Personal inforamtion ')
labelinformationPersonnel.setAlignment(QtCore.Qt.AlignCenter)
retourButtonInformationHome=buttonF(270,0,90,30,'font-size:15px;background-color:#0479f7;border:2px solid white;border-radius:15px;color:white;',informationPersonnel,"Home")

#Logine windiw -->forgort password Window
ForgortWindowPasswordApresLogine=windowF(974,615,'Verification','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\Window Securite\\PasswordChenge.jpg')
labelEmailForgortPassword=labelF(310,300,150,50,'font-size:20px;color:white;',ForgortWindowPasswordApresLogine,'Enter your email')
inputEmailForgortPassword=inputF(510,300,400,50,'border-radius:10px;background-color:#dfdfdf;font-size:25px;',ForgortWindowPasswordApresLogine,'Enter your email ')
buttonSendCodeEmailForgort=buttonF(600,370,200,50,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#cd5b51;color:white;',ForgortWindowPasswordApresLogine,"Send Code")
retourButtonFoegort_loginewindow=buttonF(10, 12,80,30,'font-size:15px;background-color:#cd5b51;border-radius:15px;color:white;',ForgortWindowPasswordApresLogine,"Back")

# Verifiet Email window Forgort Password
verWindowForgortPassword=windowF(974,615,'Verification','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
verifietCodeEmailLabel0=labelF(505,198,200, 50,'font-size:17px;',verWindowForgortPassword,"Code sent to : "+inputEmailForgortPassword.text())
inputverifietCodeEmail0=inputF(510, 250,200, 50,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#dfdfdf;',verWindowForgortPassword,"Code")
buttonVerefietCode0=buttonF(548,310,139,30,'border-radius:10px;border:2px solid #dfdfdf;font-size:20px;background-color:#cd5b51;color:white;',verWindowForgortPassword,"Next")
retourButton0=buttonF(270, 12,90, 40,'font-size:15px;background-color:#0479f7;border:2px solid white;border-radius:15px;color:white;',verWindowForgortPassword,"Back")
# Password window1
passwordWindow1=windowF(974,615,'Changing password...','YOB PROJECT\\png\\YOB.png','YOB PROJECT\\sing up\\singup.png')
labelEmailIdentifiante1=labelF(460,150,500,50,'font-size:25px;',passwordWindow1,"<u><b>Try to enter a complicated password</b></u>")
labelInputCodeIdentification1=labelF(290,220,190,50,'font-size:20px;',passwordWindow1,"Password : ")
inputCodeIdentification1=inputF(450,220,500,50,'border-radius:10px;border:2px solid #dfdfdf;font-size:28px;background-color:#dfdfdf;',passwordWindow1,"New password")
labelInputVerCodeIdentification1=labelF(290,300,190,50,'font-size:20px;',passwordWindow1,"Password : ")
inputVerCodeIdentification1=inputF(450,300,500,50,'border-radius:10px;border:2px solid #dfdfdf;font-size:28px;background-color:#dfdfdf;',passwordWindow1,"Password confirmation")
inputVerCodeIdentification1.setEchoMode(QtWidgets.QLineEdit.Password)
buttonAccesCompte=buttonF(595,380,190,50,'border-radius:10px;border:2px solid white;font-size:20px;background-color:#cd5b51;',passwordWindow1,"Confirm ")
retourButtonlogin1=buttonF(270,12,90,40,'font-size:15px;background-color:#0479f7;border:2px solid white;border-radius:15px;color:white;',passwordWindow1,"Back")


#chek internet connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

#Peobleme function
def probleme(problem):
    labelProblem.setText(problem+" !!!")
    ProblemConnetion.show()
#ForgortWindowPasswordApreslogine --> Home Window
def passwordWindow1_HomeWindow():
    if not connect():
        probleme("A network problem was detected")
    elif inputVerCodeIdentification1.text()==inputCodeIdentification1.text():
        x = returnDataApartirId(emailExeste(inputEmailForgortPassword.text()))
        changeInformation(x[0],'',inputCodeIdentification1.text())
        empiler(client, x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12])
        homewindow.show()
        passwordWindow1.close()
#password Window 1 --> ForgortWindowPasswordApreslogine
def passwordWindow1_ForgortWindowPasswordApresLogine():
    if not connect():
        probleme("A network problem was detected")
    else :
        ForgortWindowPasswordApresLogine.show()
        passwordWindow1.close()
# verifier la connection internet
if not connect():
    probleme("A network problem was detected")
else:
    logineWindow.show()
#Set Data in information Client
def setDataInformationCient():
    global client
    Sexe.setText(str(client.getSexe()))
    Phonenumber.setText(str(client.getNumeroTelephone()))
    Ville.setText(str(client.getVille()))
    Email.setText(str(client.getEmailAdress()))
    CIN.setText(str(client.getCin()))
    Solde.setText(str(client.getSoldeClient()))
    Rib.setText(str(client.getRibClient()))
    Age.setText(str(client.getAge()))
    Prenom.setText(str(client.getPrenom()))
    Nom.setText(str(client.getNom()))
    DateCreation.setText(str(client.getDateCreation()))
def comboParametree():
    if not connect():
        probleme("A network problem was detected")
    elif comboParametre.currentText()=='Edit Password' :
            editePasswordWindow.show()
            homewindow.close()
    elif comboParametre.currentText()=='Personal information':
        setDataInformationCient()
        informationPersonnel.show()
        homewindow.close()
    elif comboParametre.currentText()=='Transfer':
        transferWindow.show()
        homewindow.close()
    elif comboParametre.currentText() =='Edit phone number':
        editePhoneNumberWindow.show()
        homewindow.close()

def foegortWindow_editePasswordWindowVerifietEmail():
    if not connect():
        probleme("A network problem was detected")
    elif buttonfoegortWindow.text() == codeEmail2:
        editePasswordWindowVerifietEmail.show()
        foegortWindow.close()
    else :
        probleme("The code is incorrect")


def editePhoneNumberWindow_homewindow():
    if not connect():
        probleme("A network problem was detected")
    else:
        editePhoneNumberWindow.close()
        homewindow.show()


def editeChangePhoneNumberWindow_homewindow():
    if not connect():
        probleme("A network problem was detected")
    elif not phoneNumberverification(inputNvPhoneNumber.text()) or len(inputNvPhoneNumber.text()) < 10:
        probleme("phone number is incorrect ")
    else:
        changeInformation(client.getIdClient(),inputNvPhoneNumber.text(),'')
        client.setNumeroTelephone(inputNvPhoneNumber.text())
        inputNvPhoneNumber.setText('')
        editePhoneNumberWindow.close()
        homewindow.show()


def foegortWindow_editePasswordWindow():
    if not connect():
        probleme("A network problem was detected")
    else:
        editePasswordWindow.show()
        editePasswordWindowVerifietEmail.close()

#TRANSFER FUNCTION --> HOME WINDOW
def transfer_homewindow():
    if not connect():
        probleme("A network problem was detected")
    else:
        homewindow.show()
        transferWindow.close()
def transferApresTransfer_homewindow():
    if not connect():
        probleme("A network problem was detected")
    elif rechercheRib(inputRib.text())!=0 and phoneNumberverification(inputSendMoney.text())==True :
        x=returnDataApartirId(rechercheRib(inputRib.text()))
        empiler(clientATransere,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])
        if float(client.getSoldeClient())<float(inputSendMoney.text()):
            probleme("Your balance is : "+str(client.getSoldeClient()))
        else :
            setSolde(clientATransere.getIdClient(),float(clientATransere.getSoldeClient())+float(inputSendMoney.text()))
            SetHistorique(clientATransere.getIdClient(),"Last name : "+client.getNom()+"\nFirst name : "+client.getPrenom()+"\nBalance : "+str(inputSendMoney.text()))
            setSolde(client.getIdClient(), float(client.getSoldeClient()) - float(inputSendMoney.text()))
            client.setSoldeClient(float(client.getSoldeClient())-float(inputSendMoney.text()))
            inputSendMoney.setText('')
            homewindow.show()
            transferWindow.close()
    elif rechercheRib(inputRib.text())==0:
        probleme("This Rib : "+str(inputRib.text())+" is not existed")
    else :
        probleme(str(inputRib.text())+" (The rib should include only numbers )")
#EDITE PASSWORD --> HOME WINDOW
def editepasswdChange_homewindow():
    if not connect():
        probleme("A network problem was detected")
    elif loginDatabaseClient(client.getEmailAdress(),inputLastPassword.text())!=0 and inputNvPassword.text()==inputNvPassword2.text():
        changeInformation(client.getIdClient(),'',inputNvPassword.text())
        homewindow.show()
        editePasswordWindow.close()
    elif loginDatabaseClient(client.getEmailAdress(),inputLastPassword.text())==0:
        probleme('Old password is incorrect')
    else:
        probleme("The passwords are not identical ")
def editePasswordWindowVerifietEmail_homewindow():
    if not connect():
        probleme("A network problem was detected")
    elif inputNvPassword2VerifietCodeEmail.text()==inputNvPasswordVerifietCodeEmail.text():
        changeInformation(client.getIdClient(),'',inputNvPasswordVerifietCodeEmail.text())
        homewindow.show()
        editePasswordWindow.close()
    else:
        probleme("The passwords are not identical")
def editepasswd_homewindow():
    if not connect():
        probleme("A network problem was detected")
    else:
        homewindow.show()
        editePasswordWindow.close()
#INFORMATION PERSONNEL --> HOME WINDOW
def informationPersonnel_homewindow():
    if not connect():
        probleme("A network problem was detected")
    else:
        homewindow.show()
        informationPersonnel.close()

#LOGIN WINDOW --> SIGNE UP WINDOW
def logineWindow_signeupWindow():  # logineWindow->singupWindow
    if not connect():
        probleme("A network problem was detected")
    else:
        singupWindow.show()
        logineWindow.close()

#SING UP WINDOW --> LOGIN WINDOW
def singupWindow_logineWindow():  # singupWindow->logineWindow
    if not connect():
        probleme("A network problem was detected")
    else:
        inputIdentifiant.setText('')
        inputPassword.setText('')
        logineWindow.show()
        singupWindow.close()

#GENERATE CODE EMAIL
def codeEmail():
    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    pwd_length=4
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd
#Code Generater
codeEmail1=str(codeEmail()+str(random.randint(2000,8000))).upper()
codeEmail2=str(codeEmail()+str(random.randint(2000,8000))).upper()
#SENT EMAIL : PROTOCOLE SMTP( SIMPLE MAIL TRANSFER PROTOCOLE )
def sentEmail(email,code):  # send Email
        try:
            email_sender = 'youronlinebank.yob@gmail.com'
            email_password = 'kudhewaichrjodle'
            email_receiver = email
            subject = "Code de verification of YOB : "
            body = "Hello "+inputFirstName.text()+" in your online bank \n    Code is : " + code
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
        except:
            probleme('problem was detected.\n     Try again ')

#CONVERSION STRING --> INTEGER
def phoneNumberverification(nbr):
    try:
        x=float(nbr)
        return True
    except:
        return False
#SIGN UP WINDOW --> VEREFICATION CODE SEND IN EMAIL
def signupWindow_verWindow():  # singupWindow->verWindow
    if inputAddress.text() == '' or inputFirstName.text() == '' or inputLastName.text() == '' or inputNumberPhone.text()=='' or inputCIN.text()=='' or inputVille.currentText()=='City' or inputSex.currentText()=='Gender' or inputAge.currentText()=='Age':
        if inputAddress.text()=='':
            etoileAdressEmail.show()
        else:
            etoileAdressEmail.close()
        if inputFirstName.text()=='':
            etoileFirstName.show()
        else:
            etoileFirstName.close()
        if inputLastName.text()=='':
            etoileLastName.show()
        else:
            etoileLastName.close()
        if inputNumberPhone.text()=='':
            etoilePhoneNumber.show()
        else:
            etoilePhoneNumber.close()
        if inputCIN.text()=='':
            etoileCin.show()
        else:
            etoileCin.close()
        if inputVille.currentText()=='City' :
            etoileVille.show()
        else:
            etoileVille.close()
        if inputSex.currentText()=='Gender' :
            etoileSex.show()
        else:
            etoileSex.close()
        if inputAge.currentText()=='Age':
            etoileAge.show()
        else:
            etoileAge.close()
    elif not connect():
        probleme("A network problem was detected")
    elif not phoneNumberverification(inputNumberPhone.text()) or len(inputNumberPhone.text())<10:
        probleme("Phone number is incorrect")
    elif len(inputCIN.text())!=8:
        probleme("Id card is incorrect ")
    elif emailExeste(inputAddress.text())!=0:
        probleme("This email :"+str(inputAddress.text())+" is already existed")
    else:
        sentEmail(inputAddress.text(),codeEmail1)
        verWindow.show()
        singupWindow.close()
#Forgort Window --> Verifiete password Window
def ForgortWindowPasswordApresLogine_verWindowForgortPassword():
    if not connect():
        probleme("A network problem was detected ")
    elif emailExeste(inputEmailForgortPassword.text())!=0:
        sentEmail(inputEmailForgortPassword.text(),codeEmail2)
        labelEmailIdentifiante.setText(inputEmailForgortPassword.text())
        verWindowForgortPassword.show()
        ForgortWindowPasswordApresLogine.close()
    else:
        probleme('This email : '+inputEmailForgortPassword.text()+" is not existed")
#Login Window --> Forgort password
def loginwindow_Forgortwindow():
    if not connect():
        probleme('A network problem was detected')
    else:
        ForgortWindowPasswordApresLogine.show()
        logineWindow.close()
#Login Window --> Forgort password
def verWindowForgortPassword_ForgortWindowPasswordApresLogine():
    if not connect():
        probleme('A network problem was detected')
    else:
        ForgortWindowPasswordApresLogine.show()
        verWindowForgortPassword.close()
#ForgortWindowPasswordApresLogine --> LogineWindow
def ForgortWindowPasswordApresLogine_logineWindow():
    if not connect():
        probleme('A network problem was detected ')
    else:
        logineWindow.show()
        ForgortWindowPasswordApresLogine.close()

#Edite Password --> Forgort PASSWORD
def editepasswd_forgortpasswd():
    if not connect():
        probleme("A network problem was detected")
    else:
        sentEmail(client.getEmailAdress(),codeEmail2)
        foegortWindow.show()
        editePasswordWindow.close()

#FORGORT PASSWORD --> Edite Password Window
def forgortpasswd_editepasswd():
    if not connect():
        probleme("A network problem was detected")
    else:
        editePasswordWindow.show()
        foegortWindow.close()

#Verfifiet Code Send In Email --> Sign Up window
def verWindow_singupWindow():  # verWindow->singupWindow
    if not connect():
        probleme("A network problem was detected")
    else:
        singupWindow.show()
        verWindow.close()

#Verifiete Code sent in Your Email --> Password Window
def verWindow_passwordWindow():  # verWindow->mainWindow
    if not connect():
        probleme("A network problem was detected")
    elif inputverifietCodeEmail.text()== codeEmail1 :
        passwordWindow.show()
        verWindow.close()
    else:
        inputverifietCodeEmail.setText('')
        probleme("The code is incorrect")
#Verifiete Code sent in Your Email --> Password Window Apres verfiet code email forgort password
def verWindowForgortPassword_passwordWindow1():  # verWindow Apres login->mainWindow
    if not connect():
        probleme("A network problem was detected")
    elif inputverifietCodeEmail0.text()==codeEmail2:
        passwordWindow1.show()
        verWindowForgortPassword.close()
    else:
        inputverifietCodeEmail0.setText('')
        probleme("The code is incorrect")
#Creat Compt
def creatCompte(): #passwordWindow->homewindow
    if not connect():
        probleme("A network problem was detected")
    elif inputVerCodeIdentification.text()=='' or inputCodeIdentification.text()=='':
        if inputVerCodeIdentification.text()=='':
            etoilelabelInputVerCodeIdentification.show()
        else:
            etoilelabelInputVerCodeIdentification.close()
        if inputCodeIdentification.text()=='':
            etoilelabelInputCodeIdentification.show()
        else:
            etoilelabelInputCodeIdentification.close()
    elif inputVerCodeIdentification.text()==inputCodeIdentification.text():
        rib = str(random.randint(3000, 4000)) + str(random.randint(1000, 8000))
        while rechercheRib(rib) != 0:
            rib = str(random.randint(3000, 4000)) + str(random.randint(1000, 8000))
        insert_personne(inputFirstName.text(), inputLastName.text(), inputAge.currentText(), inputCIN.text(),inputAddress.text(), inputNumberPhone.text(), inputVille.currentText(), inputSex.currentText(),rib, 0,inputVerCodeIdentification.text() )
        x=returnDataApartirId(emailExeste(inputAddress.text()))
        empiler(client,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])
        inputFirstName.setText('')
        inputLastName.setText('')
        inputAge.setCurrentText('')
        inputCIN.setText('')
        inputAddress.setText('')
        inputNumberPhone.setText('')
        inputVille.setCurrentText('')
        inputSex.setCurrentText('')
        inputVerCodeIdentification.setText('')
        inputCodeIdentification.setText('')
        homewindow.show()
        passwordWindow.close()
    else :
        probleme("The passwords are not identical")
#Client Empiler
def empiler(clientS,idClient,nom,prenom,age,cin,emailAdress,telephone,ville,sexe,rib,solde,password,date_Creation):
    clientS.setIdClient(idClient)
    clientS.setNom(nom)
    clientS.setPrenom(prenom)
    clientS.setAge(age)
    clientS.setCin(cin)
    clientS.setEmailAdress(emailAdress)
    clientS.setNumeroTelephone(telephone)
    clientS.setVille(ville)
    clientS.setSexe(sexe)
    clientS.setRibClient(rib)
    clientS.setSoldeClient(solde)
    clientS.setPassword(password)
    clientS.setDateCreation(date_Creation)
# login button function
def logineWindow_homeWindow():
    if not connect():
        probleme("A network problem was detected")
    elif loginDatabaseClient(inputIdentifiant.text(),inputPassword.text())!=0:
        x=returnDataApartirId(loginDatabaseClient(inputIdentifiant.text(),inputPassword.text()))
        empiler(client,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])
        inputIdentifiant.setText('')
        inputPassword.setText('')
        homewindow.show()
        logineWindow.close()
    else:
        probleme("Information is incorrect")
#PasswordWindow-->SignUp Window
def passwordWindow_singupWindow(): # passwordWindow->signupwindow
    singupWindow.show()
    passwordWindow.close()

def showHomewindow():
    homewindow.close()
    homewindow.show()
#CONNECTIVITE
buttonSendCodeEmailForgort.clicked.connect(ForgortWindowPasswordApresLogine_verWindowForgortPassword)
signupButton.clicked.connect(logineWindow_signeupWindow)
retourButton.clicked.connect(singupWindow_logineWindow)
buttonVerefietCode.clicked.connect(verWindow_passwordWindow)
signUpNow.clicked.connect(signupWindow_verWindow)
retourButton1.clicked.connect(verWindow_singupWindow)
buttonCreatCompte.clicked.connect(creatCompte)
loginButton.clicked.connect(logineWindow_homeWindow)
retourButtonlogin.clicked.connect(passwordWindow_singupWindow)
buttonHome.clicked.connect(showHomewindow)
comboParametre.activated.connect(comboParametree)
retourButtonTransferHome.clicked.connect(transfer_homewindow)
retourButtonEditepasswdHome.clicked.connect(editepasswd_homewindow)
retourButtonInformationHome.clicked.connect(informationPersonnel_homewindow)
retourButtonFoegort_editepasswd.clicked.connect(forgortpasswd_editepasswd)
forgortpasswd.clicked.connect(editepasswd_forgortpasswd)
buttonfoegortWindow.clicked.connect(foegortWindow_editePasswordWindowVerifietEmail)
retourButtonEditePasswordWindowVerifietEmail_Home.clicked.connect(foegortWindow_editePasswordWindow)
retourButtoneditePhonenumberWindowHomewindow.clicked.connect(editePhoneNumberWindow_homewindow)
buttonchangePhoneWindow.clicked.connect(editeChangePhoneNumberWindow_homewindow)
forgortpassword.clicked.connect(loginwindow_Forgortwindow)
retourButtonFoegort_loginewindow.clicked.connect(ForgortWindowPasswordApresLogine_logineWindow)
retourButton0.clicked.connect(verWindowForgortPassword_ForgortWindowPasswordApresLogine)
buttonVerefietCode0.clicked.connect(verWindowForgortPassword_passwordWindow1)
ChangeButton.clicked.connect(editepasswdChange_homewindow)
sendButton.clicked.connect(transferApresTransfer_homewindow)
ChangeButtonVerifietCodeEmail.clicked.connect(editePasswordWindowVerifietEmail_homewindow)
retourButtonlogin1.clicked.connect(passwordWindow1_ForgortWindowPasswordApresLogine)
buttonAccesCompte.clicked.connect(passwordWindow1_HomeWindow)

YOB.exec_()