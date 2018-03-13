import sqlite3
import csv

class Test:
    conn = sqlite3.connect('ma_base.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Installation(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,NomInstallation TEXT,NumInstallation INTEGER,NomCommune TEXT,CodeInsee INTEGER,CodePostal INTEGER,NomLieu TEXT,NumVoie INTEGER,NomVoie TEXT,Location TEXT,Longitude INTEGER,Latitude INTEGER,AucunAménagementAcces TEXT,AccessibiliHandicapReduite TEXT,AccessibiliMobRed TEXT,AccessibiliSensoriel TEXT,EmpriseFonctière INTEGER,Gardiennée TEXT,MultiCommune TEXT,Internet TEXT,NbCouvert INTEGER,NbLit INTEGER,NbTotalPlace INTEGER,NbTotalPlaceHandicapé INTEGER,InstallationParticulière INTEGER,DesserteMetro TEXT,DesserteBus TEXT,DesserteTram TEXT,DesserteBateau TEXT,DesserteAutre TEXT,NbTotalEquipementSportif INTEGER,NbTotalEquipementFiche INTEGER,DateCreationFiche TEXT,DateMajFiche TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Activities(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,ComInsee TEXT,ComLib TEXT,EquipementId INTEGER,EquNbEquIdentique TEXT,ActCode TEXT,ActLib TEXT,EquActivitePraticable TEXT,EquActivitePratique TEXT,EquActiviteSalleSpe TEXT,ActNivLib TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Equipements(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, ComInsee TEXT,ComLib TEXT,InsNumeroInstall TEXT,InsNom TEXT,EquipementId TEXT,EquNom TEXT,EquNomBatiment TEXT,EquNbEquIdentique TEXT,EquipementTypeCode TEXT,EquipementTypeLib TEXT,GestionTypeProprietairePrincLib TEXT,GestionTypeGestionnairePrincLib TEXT,GestionTypeProprietaireSecLib TEXT,GestionTypeGestionnaireSecLib TEXT,EquGestionDSP TEXT,EquDouche TEXT,EquEclairage TEXT,EquErpCTS TEXT,EquErpREF TEXT,EquErpL TEXT,EquErpN TEXT,EquErpO TEXT,EquErpOA TEXT,EquErpP TEXT,EquErpPA TEXT,EquErpR TEXT,EquErpRPE TEXT,EquErpSG TEXT,EquErpX TEXT,EquErpCategorie TEXT,EquAnneeService TEXT,AnneeServiceLib TEXT,EquNbPlaceTribune TEXT,NatureSolLib TEXT,NatureLibelle TEXT,EquHauteurEvolution TEXT,EquLongueurEvolution TEXT,EquLargeurEvolution TEXT,EquSurfaceEvolution TEXT,EquHauteurSurfaceEvo TEXT,EquNbCouloirPiste TEXT,EquNbVestiaireSpo TEXT,EquVestiaireSpoChauffe TEXT,EquNbVestiaireArbitre TEXT,EquSanitaireSportif TEXT,EquSanitairePublic TEXT,EquOuvertSaison TEXT,EquProximite TEXT,EquSono TEXT,EquTableauFixe TEXT,EquChrono TEXT,EquAmenagementAucun TEXT,EquUtilScolaire TEXT,EquUtilClub TEXT,EquUtilAutre TEXT,EquUtilIndividuel TEXT,EquUtilPerformance TEXT,EquUtilFormation TEXT,EquUtilRecreation TEXT,EquDateDernierTravauxReal TEXT,AnneeTravauxRealLibelle TEXT,EquDateDernierTravauxAucun TEXT,EquTravauxRealConformite TEXT,EquTravauxRealNorme TEXT,EquTravauxRealUsager TEXT,EquTravauxRealDegradation TEXT,EquTravauxRealVetuste TEXT,EquAccesHandimAire TEXT,EquAccesHandimTribune TEXT,EquAccesHandimVestiaire TEXT,EquAccesHandimSaniSpo TEXT,EquAccesHandimSaniPub TEXT,EquAccesHandimAucun TEXT,EquAccesHandisAucun TEXT,EquAccesHandisAire TEXT,EquAccesHandisTribune TEXT,EquAccesHandisVestiaire TEXT,EquAccesHandisSaniSpo TEXT,EquAccesHandisSaniPub TEXT,EquAccueilClub TEXT,EquAccueilSalle TEXT,EquAccueilBuvette TEXT,EquAccueilDopage TEXT,EquAccueilMedic TEXT,EquAccueilInfirmerie TEXT,EquAccueilBureau TEXT,EquAccueilReception TEXT,EquAccueilLocalRangement TEXT,EquAccueilAutre TEXT,EquAccueilAucun TEXT,EquChauffageNon TEXT,EquChauffageFuel TEXT,EquChauffageGaz TEXT,EquChauffageElectricite TEXT,EquChauffageSolaire TEXT,EquChauffageAutre TEXT,EquConfortSauna TEXT,EquConfortBainBouillonant TEXT,EquConfortBainVapeur TEXT,EquConfortSolarium TEXT,EquConfortAutre TEXT,EquConfortAucun TEXT,EquDemarcheHQE TEXT,EquSaeNbCouloir TEXT,EquSaeHauteur TEXT,EquSaeSurface TEXT,EquNatureSignal TEXT,EquNatureAlert TEXT,EquNatureAcPubPed TEXT,EquNatureAcPubRout TEXT,EquNatureAcPubMec TEXT,EquNatureAcPubNau TEXT,EquNatureAcSecPed TEXT,EquNatureAcSecRout TEXT,EquNatureAcSecMec TEXT,EquNatureAcSecNau TEXT,EquNatureLocTec TEXT,EquNatureLocPed TEXT,EquNatureAutorise TEXT,EquNaturePDESI TEXT,EquipNatureSituationLib TEXT,EquNatureSEVoies TEXT,EquNatureClassFedeMini TEXT,EquNatureClassFedeMaxi TEXT,EquNatureESTour TEXT,EquNatureAETreuil TEXT,EquNatureSKTotalRemontee TEXT,EquipementTir10 TEXT,EquipementTir25 TEXT,EquipementTir50 TEXT,EquipementTir100 TEXT,EquipementTir200 TEXT,EquipementTir300 TEXT,EquipementTirPlateau TEXT,EquipementTirAutre TEXT,EquAthDev TEXT,EquAthLongLigneDroite TEXT,EquAthNbCouloirLigne TEXT,EquAthNbCouloirHorsLigne TEXT,EquAthRiviere TEXT,EquNatSurv TEXT,EquAthNbSautTotal TEXT,EquAthNbSautHauteur TEXT,EquAthNbSautLongueur TEXT,EquAthNbSautTriple TEXT,EquAthNbSautPerche TEXT,EquAthNbLancerTotal TEXT,EquAthNbPoids TEXT,EquAthNbDisque TEXT,EquAthNbJavelot TEXT,EquAthNbMarteau TEXT,EquAthNBMarteauMixte TEXT,EquNatFormeLib TEXT,EquNatLongueurBassin TEXT,EquNatLargeurBassin TEXT,EquNatSurfaceBassin TEXT,EquNatProfMini TEXT,EquNatProfMax TEXT,EquNatCouloir TEXT,EquNatSurfacePlageBassin TEXT,EquNatNbTTotal TEXT,EquNatNbT1 TEXT,EquNatNbT3 TEXT,EquNatNbPTotal TEXT,EquNatNbP3 TEXT,EquNatNbP5 TEXT,EquNatNbP7 TEXT,EquNatNbP10 TEXT,EquNatMaV TEXT,EquNatTobog TEXT,EquNatPentaglisse TEXT,EquNatRiviere TEXT,EquNatImHandi TEXT,EquNatFM TEXT,EquNatMM TEXT,EquNatEclSub TEXT,EquNatSonorisationSub TEXT,EquNatAutre TEXT,EquPresencePataugeoir TEXT,EquGpsX TEXT,EquGpsY TEXT,EquDateCreation TEXT,EquDateMaj TEXT)')
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
                    cursor.execute('INSERT INTO Installation(NomInstallation,NumInstallation,NomCommune,CodeInsee,CodePostal,NomLieu,NumVoie,NomVoie,Location,Longitude,Latitude,AucunAménagementAcces,AccessibiliHandicapReduite,AccessibiliMobRed,AccessibiliSensoriel,EmpriseFonctière,Gardiennée,MultiCommune,Internet,NbCouvert,NbLit,NbTotalPlace,NbTotalPlaceHandicapé,InstallationParticulière,DesserteMetro,DesserteBus,DesserteTram,DesserteBateau,DesserteAutre,NbTotalEquipementSportif,NbTotalEquipementFiche,DateCreationFiche,DateMajFiche) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',line)
                    conn.commit()
        if fichier=="2":
            with open('equipements.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    cursor.execute('INSERT INTO Equipements(ComInsee,ComLib,InsNumeroInstall,InsNom,EquipementId,EquNom,EquNomBatiment,EquNbEquIdentique,EquipementTypeCode,EquipementTypeLib,GestionTypeProprietairePrincLib,GestionTypeGestionnairePrincLib,GestionTypeProprietaireSecLib,GestionTypeGestionnaireSecLib,EquGestionDSP,EquDouche,EquEclairage,EquErpCTS,EquErpREF,EquErpL,EquErpN,EquErpO,EquErpOA,EquErpP,EquErpPA,EquErpR,EquErpRPE,EquErpSG,EquErpX,EquErpCategorie,EquAnneeService,AnneeServiceLib,EquNbPlaceTribune,NatureSolLib,NatureLibelle,EquHauteurEvolution,EquLongueurEvolution,EquLargeurEvolution,EquSurfaceEvolution,EquHauteurSurfaceEvo,EquNbCouloirPiste,EquNbVestiaireSpo,EquVestiaireSpoChauffe,EquNbVestiaireArbitre,EquSanitaireSportif,EquSanitairePublic,EquOuvertSaison,EquProximite,EquSono,EquTableauFixe,EquChrono,EquAmenagementAucun,EquUtilScolaire,EquUtilClub,EquUtilAutre,EquUtilIndividuel,EquUtilPerformance,EquUtilFormation,EquUtilRecreation,EquDateDernierTravauxReal,AnneeTravauxRealLibelle,EquDateDernierTravauxAucun,EquTravauxRealConformite,EquTravauxRealNorme,EquTravauxRealUsager,EquTravauxRealDegradation,EquTravauxRealVetuste,EquAccesHandimAire,EquAccesHandimTribune,EquAccesHandimVestiaire,EquAccesHandimSaniSpo,EquAccesHandimSaniPub,EquAccesHandimAucun,EquAccesHandisAucun,EquAccesHandisAire,EquAccesHandisTribune,EquAccesHandisVestiaire,EquAccesHandisSaniSpo,EquAccesHandisSaniPub,EquAccueilClub,EquAccueilSalle,EquAccueilBuvette,EquAccueilDopage,EquAccueilMedic,EquAccueilInfirmerie,EquAccueilBureau,EquAccueilReception,EquAccueilLocalRangement,EquAccueilAutre,EquAccueilAucun,EquChauffageNon,EquChauffageFuel,EquChauffageGaz,EquChauffageElectricite,EquChauffageSolaire,EquChauffageAutre,EquConfortSauna,EquConfortBainBouillonant,EquConfortBainVapeur,EquConfortSolarium,EquConfortAutre,EquConfortAucun,EquDemarcheHQE,EquSaeNbCouloir,EquSaeHauteur,EquSaeSurface,EquNatureSignal,EquNatureAlert,EquNatureAcPubPed,EquNatureAcPubRout,EquNatureAcPubMec,EquNatureAcPubNau,EquNatureAcSecPed,EquNatureAcSecRout,EquNatureAcSecMec,EquNatureAcSecNau,EquNatureLocTec,EquNatureLocPed,EquNatureAutorise,EquNaturePDESI,EquipNatureSituationLib,EquNatureSEVoies,EquNatureClassFedeMini,EquNatureClassFedeMaxi,EquNatureESTour,EquNatureAETreuil,EquNatureSKTotalRemontee,EquipementTir10,EquipementTir25,EquipementTir50,EquipementTir100,EquipementTir200,EquipementTir300,EquipementTirPlateau,EquipementTirAutre,EquAthDev,EquAthLongLigneDroite,EquAthNbCouloirLigne,EquAthNbCouloirHorsLigne,EquAthRiviere,EquNatSurv,EquAthNbSautTotal,EquAthNbSautHauteur,EquAthNbSautLongueur,EquAthNbSautTriple,EquAthNbSautPerche,EquAthNbLancerTotal,EquAthNbPoids,EquAthNbDisque,EquAthNbJavelot,EquAthNbMarteau,EquAthNBMarteauMixte,EquNatFormeLib,EquNatLongueurBassin,EquNatLargeurBassin,EquNatSurfaceBassin,EquNatProfMini,EquNatProfMax,EquNatCouloir,EquNatSurfacePlageBassin,EquNatNbTTotal,EquNatNbT1,EquNatNbT3,EquNatNbPTotal,EquNatNbP3,EquNatNbP5,EquNatNbP7,EquNatNbP10,EquNatMaV,EquNatTobog,EquNatPentaglisse,EquNatRiviere,EquNatImHandi,EquNatFM,EquNatMM,EquNatEclSub,EquNatSonorisationSub,EquNatAutre,EquPresencePataugeoir,EquGpsX,EquGpsY,EquDateCreation,EquDateMaj) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',line)
                    conn.commit()
        if fichier=="3":
            with open('J334_equipements_activites.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    cursor.execute('INSERT INTO Activities(ComInsee,ComLib,EquipementId,EquNbEquIdentique,ActCode,ActLib,EquActivitePraticable,EquActivitePratique,EquActiviteSalleSpe,ActNivLib) VALUES(?,?,?,?,?,?,?,?,?,?)',line)
                    conn.commit()

    def get_posts(self,fichier):
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        if fichier=="1":
            lines = cursor.execute("select * from Installation")
            while True:
                row = cursor.fetchone()
                print(row)
                if row == None: break
            conn.close()
        if fichier=="2":
            lines = cursor.execute("select * from Equipements")
            while True:
                row = cursor.fetchone()
                print(row)
                if row == None: break
            conn.close()
        if fichier=="3":
            lines = cursor.execute("select * from Activities")
            while True:
                row = cursor.fetchone()
                print(row)
                if row == None: break
            conn.close()

    def getbyNomInstallation(self,fichier):
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        if fichier=="1":
            print("Saisir le nom de l'installation que vous recherchez :")
            saisie = input()
            lines = cursor.execute('''select * from Installation where NomInstallation=?''', (saisie,))
            while True:
                row = cursor.fetchone()
                print(row)
                if row == None: break
            conn.close()
        if fichier=="2":
            print("Saisir le nom de la commune que vous recherchez :")
            saisie = input()
            lines = cursor.execute('''select * from Installation where NomCommune=?''', (saisie,))
            while True:
                row = cursor.fetchone()
                print(row)
                if row == None: break
            conn.close()

    def menu(self):
        print("-----Hello-----")
        print("1.Afficher")
        print("2.Importer CSV")
        print("3.Recherche")
        print("4.Quitter")
        print("Saisir votre choix :")
        saisie = input()
        if saisie == "1":
            print("Saisir le num de la liste à afficher :")
            print("1.Installations")
            print("2.Equipements")
            print("3.Activités")
            fichier=input()
            if fichier=="1":
                self.get_posts("1")
                self.menu()
            elif fichier=="2":
                self.get_posts("2")
                self.menu()
            elif fichier == "3":
                self.get_posts("3")
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
                self.importintobd("3")
                self.menu()
        elif saisie == "3":
            print("Choisir votre type de recherche :")
            print("1.Recherche par nom d'installation")
            print("2.Recherche par commune")
            num=input()
            if num=="1":
                self.getbyNomInstallation("1")
                self.menu()
            elif num=="2":
                self.getbyNomInstallation("2")
                self.menu()
        elif saisie=="4":
            print("Bye !")
            exit(0)
        elif saisie!="1"or"2"or"3"or"4":
            print("Mauvaise touche veuillez recommencer")
            self.menu()

ex = Test()
ex.menu()

