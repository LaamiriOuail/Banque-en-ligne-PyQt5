class Personne:
    def __init__(self,nom,prenom,age,cin,emailAdress,numeroTelephone,ville,sexe):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
        self.__cin=cin
        self.__emailAdress=emailAdress
        self.__numeroTelephone=numeroTelephone
        self.__ville=ville
        self.__sexe=sexe
    #getters
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getAge(self):
        return self.__age
    def getCin(self):
        return self.__cin
    def getEmailAdress(self):
        return self.__emailAdress
    def getNumeroTelephone(self):
        return self.__numeroTelephone
    def getVille(self):
        return self.__ville
    def getSexe(self):
        return self.__sexe
    #Setters
    def setNom(self,nom):
        self.__nom=nom
    def setPrenom(self,prenom):
        self.__prenom=prenom
    def setAge(self,age):
        self.__age=age
    def setCin(self,cin):
        self.__cin=cin
    def SetEmailAdress(self,emailAdress):
        self.__emailAdress=emailAdress
    def setNumeroTelephone(self,numeroTelephone):
        self.__numeroTelephone=numeroTelephone
    def setVille(self,ville):
        self.__ville=ville
    def setSexe(self,sexe):
        self.__sexe=sexe
    def setEmailAdress(self,emailAdress):
        self.__emailAdress=emailAdress



class Client(Personne):
    def __init__(self,nom,prenom,age,cin,emailAdress,numeroTelephone,ville,sexe,idClient,ribClient,soldeClient,password,dateCreation):
        self.setNom(nom)
        self.setPrenom(prenom)
        self.setCin(cin)
        self.setAge(age)
        self.setVille(ville)
        self.setNumeroTelephone(numeroTelephone)
        self.setSexe(sexe)
        self.setEmailAdress(emailAdress)
        self.__idClient=idClient
        self.__ribClient=ribClient
        self.__soldeClient=soldeClient
        self.__password=password
        self.__dateCreation=dateCreation
    #Getters
    def getDateCreation(self):
        return self.__dateCreation
    def getIdClient(self):
        return self.__idClient
    def getRibClient(self):
        return self.__ribClient
    def getSoldeClient(self):
        return self.__soldeClient
    def getPassword(self):
        return self.__password
    #Setters
    def setIdClient(self,idClient):
         self.__idClient=idClient
    def setDateCreation(self,dateCreation):
        self.__dateCreation=dateCreation
    def setRibClient(self,ribClient):
        self.__ribClient=ribClient

    def setSoldeClient(self,soldeClient):
        self.__soldeClient=soldeClient

    def setPassword(self,password):
        self.__password=password
