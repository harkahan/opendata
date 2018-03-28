import sqlite3

class traitement:
    conn = sqlite3.connect('ma_base.db')

    """La fonction getbyVille permet de faire des recherches au sein de la/les base(s) de donnée"""
    def getbyVille(self,fichier,ville):
        self.resinstallations=[]
        self.resactivites=[]
        self.resequipements=[]
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        if fichier == "Installation":
            lines = cursor.execute('''select * from Installation where NomCommune=?''', (ville,))
            while True:
                row = cursor.fetchone()
                self.resinstallations.append(row)
                if row == None : break
            return (self.resinstallations)
            conn.close()
        if fichier == "Activities":
            lines = cursor.execute('''select * from Activities where ComLib=?''', (ville,))
            while True:
                row = cursor.fetchone()
                self.resactivites.append(row)
                if row == None : break
            return(self.resactivites)
            conn.close()
        if fichier == "Equipements":
            lines = cursor.execute('''select * from Equipements where ComLib=?''', (ville,))
            while True:
                row = cursor.fetchone()
                self.resequipements.append(row)
                if row == None : break
            return(self.resequipements)
            conn.close()

    def getTable(self,fichier):
        self.res1=[]
        self.res2=[]
        self.res3=[]
        conn = sqlite3.connect('ma_base.db')
        cursor = conn.cursor()
        if fichier == "Installation":
            lines = cursor.execute("select * from Installation")
            while True:
                row = cursor.fetchone()
                self.res1.append(row)
                if row == None: break
            print(self.res1)
            conn.close()
        if fichier == "Activities":
            lines = cursor.execute("select * from Activities")
            while True:
                row = cursor.fetchone()
                self.res2.append(row)
                if row == None: break
            print(self.res2)
            conn.close()
        if fichier == "Equipements":
            lines = cursor.execute("select * from Equipements")
            while True:
                row = cursor.fetchone()
                self.res3.append(row)
                if row == None: break
            print(self.res3)
            conn.close()