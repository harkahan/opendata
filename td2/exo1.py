import sqlite3
import csv

class Test:
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Installation(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,NomInstallation TEXT,NumInstallation INTEGER,NomCommune TEXT,CodeInsee INTEGER,CodePostal INTEGER,NomLieu TEXT,NumVoie INTEGER,NomVoie TEXT,Location TEXT,Longitude INTEGER,Latitude INTEGER,AucunAménagementAcces TEXT,AccessibiliHandicapReduite TEXT,AccessibiliMobRed TEXT,AccessibiliSensoriel TEXT,EmpriseFonctière INTEGER,Gardiennée TEXT,MultiCommune TEXT,Internet TEXT,NbCouvert INTEGER,NbLit INTEGER,NbTotalPlace INTEGER,NbTotalPlaceHandicapé INTEGER,InstallationParticulière INTEGER,DesserteMetro TEXT,DesserteBus TEXT,DesserteTram TEXT,DesserteBateau TEXT,DesserteAutre TEXT,NbTotalEquipementSportif INTEGER,NbTotalEquipementFiche INTEGER,DateCreationFiche TEXT,DateMajFiche TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Activities(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,ComInsee TEXT,ComLib TEXT,EquipementId INTEGER,EquNbEquIdentique TEXT,ActCode TEXT,ActLib TEXT,EquActivitePraticable TEXT,EquActivitePratique TEXT,EquActiviteSalleSpe TEXT,ActNivLib TEXT)')
    conn.commit()
    conn.close()



    table = []
    equipements = []
    activites = []

    def __init__(self):
        self.table=[]
        self.equipements=[]
        self.activites=[]

    def affichage(self,fichier):
        if fichier=="1":
            with open('23440003400026_J335_installations_table.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(', '.join(row))

        elif fichier=="2":
            with open('equipements.csv', newline='') as csvfile:

                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(', '.join(row))

        elif fichier=="3":
            with open('J334_equipements_activites.csv', newline='') as csvfile:

                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(', '.join(row))

    def importcsv(self, filename,fichier):
        fname = filename
        file = open(fname, "r")
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        try:
            reader = csv.reader(file)
            for row in reader:
                if fichier=="1":
                    self.table.append(row)
                    print(row)
                elif fichier=="2":
                    self.equipements.append(row)
                    print(row)
                elif fichier=="3":
                    self.activites.append(row)
                    print(row)
        finally:
            file.close()

    def importintobd(self,fichier):
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        if fichier=="1":
            with open('23440003400026_J335_installations_table.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    cursor.execute('INSERT INTO Installation(NumInstallation,NomInstallation,NomCommune,CodeInsee,CodePostal,NomLieu,NumVoie,NomVoie,Location,Longitude,Latitude,AucunAménagementAcces,AccessibiliHandicapReduite,AccessibiliMobRed,AccessibiliSensoriel,EmpriseFonctière,Gardiennée,MultiCommune,Internet,NbCouvert,NbLit,NbTotalPlace,NbTotalPlaceHandicapé,InstallationParticulière,DesserteMetro,DesserteBus,DesserteTram,DesserteBateau,DesserteAutre,NbTotalEquipementSportif,NbTotalEquipementFiche,DateCreationFiche,DateMajFiche) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',line)
                    conn.commit()
        if fichier=="3":
            with open('J334_equipements_activites.csv.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    cursor.execute('INSERT INTO Activities(ComInsee,ComLib,EquipementId,EquNbEquIdentique,ActCode,ActLib,EquActivitePraticable,EquActivitePratique,EquActiviteSalleSpe,ActNivLib) VALUES(?,?,?,?,?,?,?,?,?,?)',line)
                    conn.commit()
        #cursor.executemany("""
        #INSERT INTO Installation(NumInstallation,NomInstallation,NomCommune,CodeInsee,CodePostal,NomLieu,NumVoie,NomVoie,Location,
        #Longitude,Latitude,AucunAménagementAcces,AccessibiliHandicapReduite,AccessibiliMobRed,AccessibiliSensoriel,
        #EmpriseFonctière,Gardiennée,MultiCommune,Internet,NbCouvert,NbLit,NbTotalPlace,NbTotalPlaceHandicapé,InstallationParticulière,
        #DesserteMetro,DesserteBus,DesserteTram,DesserteBateau,DesserteAutre,NbTotalEquipementSportif,NbTotalEquipementFiche,DateCreationFiche,
        #DateMajFiche) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        #""",
        #self.table)

    def get_posts(self):
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        with conn:
            cursor.execute("SELECT * FROM Installation")
            print(cursor.fetchall())

    def menu(self):
        print("-----Hello-----")
        print("1.Afficher")
        print("2.Importer CSV")
        print("3.Quitter")
        print("Saisir votre choix :")
        saisie = input()
        if saisie == "1":
            print("Saisir le num de la liste à afficher :")
            print("1.Installations")
            print("2.Equipements")
            print("3.Activités")
            fichier=input()
            if fichier=="1":
                self.get_posts()
                self.menu()
            elif fichier=="2":
                self.affichage("2")
                self.menu()
            elif fichier == "3":
                self.affichage("3")
                self.menu()
        elif saisie=="2":
            print("Saisir le num de la liste à importer :")
            print("1.Installations")
            print("2.Equipements")
            print("3.Activités")
            num=input()
            if num=="1":
                self.importcsv("23440003400026_J335_installations_table.csv",num)
                self.importintobd("1")
                self.menu()
            elif num=="2":
                self.importcsv("equipements.csv", num)
                self.importintobd("2")
                self.menu()
            elif num=="3":
                self.importcsv("J334_equipements_activites.csv",num)
                self.menu()
        elif saisie=="3":
            print("Bye !")
            exit(0)
        elif saisie!="1"or"2"or"3":
            print("Mauvaise touche veuillez recommencer")
            self.menu()

ex = Test()
ex.menu()

