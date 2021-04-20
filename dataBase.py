import sqlite3
from datetime import datetime
class AudioFiles:
    def create_table(self, fileType):
        try:
            if fileType =="Audio":
            
                conn = sqlite3.connect('AudioFiles.db')
                print("Connected succesfully")
                conn.execute('''CREATE TABLE Audio 
                        (ID INT PRIMARY KEY     NOT NULL,
                            NAME           TEXT varchar(100)   NOT NULL,
                            Duration            INT     NOT NULL,
                            Uploaded_time       varchar(50)  NOT NULL);''')
                conn.close()
            elif fileType =="Podcast":
                
                conn = sqlite3.connect('AudioFiles.db')
                
                conn.execute('''CREATE TABLE Podcast 
                        (ID INT PRIMARY KEY     NOT NULL,
                            NAME_of_podcast           TEXT varchar(100)   NOT NULL,
                            Duration            INT     NOT NULL,
                            Uploaded_time       varchar(50)  NOT NULL,
                            Host           TEXT varchar(100)   NOT NULL,
                            participants varchar(100));''')
                conn.close()
            elif fileType =="AudioBook":
                # print("in first line")
                conn = sqlite3.connect('AudioFiles.db')
                # print("Connected succesfully")
                conn.execute('''CREATE TABLE AudioBook 
                        (ID INT PRIMARY KEY     NOT NULL,
                            Audiobook_title           TEXT varchar(100)   NOT NULL,
                            Author_of_title           TEXT varchar(100)   NOT NULL,
                            Narrator           TEXT varchar(100)   NOT NULL,
                            Duration            INT     NOT NULL,
                            Uploaded_time       varchar(50)  NOT NULL);''')
                conn.close()
                return "Table created"
        except Exception as e:
            return e      

    def insertAudio(self, a,b,c,d):
        try:
            try:
                if int(c) < 0:
                    return "Duration can not be in negative"
                present = datetime.now()
                given_date=list(map(int, d.split('-')))
                if datetime(*given_date) < present:
                    return "Uploaded time can not be in past"
                with sqlite3.connect("AudioFiles.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Audio VALUES (?,?,?,?)",(a,b,c,d) )
                    con.commit()
                    msg = "Record successfully added"
                    con.close()
                    print(msg)
            except:
                con.rollback()
                msg = "error in insert operation"
                print(msg)
        except Exception as e:
            return e
    def insertPodcast(self, a,b,c,d,e,f):
        try:
            if int(c) < 0:
                return "Duration can not be in negative"
            present = datetime.now()
            given_date=list(map(int, d.split('-')))
            if datetime(*given_date) < present:
                return "Uploaded time can not be in past"
            with sqlite3.connect("AudioFiles.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Podcast VALUES (?,?,?,?,?,?)",(a,b,c,d,e,f) )
                con.commit()
                msg = "Record successfully added"
                con.close()
                print(msg)
        except Exception as e:
            msg = e
        return msg
    
    def insertAudioBook(self, a,b,c,d,e,f):
        try:
            if int(e) < 0:
                return "Duration can not be in negative"
            present = datetime.now()
            given_date=list(map(int, f.split('-')))
            if datetime(*given_date) < present:
                return "Uploaded time can not be in past"

            with sqlite3.connect("AudioFiles.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO AudioBook VALUES (?,?,?,?,?,?)",(a,b,c,d,e,f) )
                con.commit()
                msg = "Record successfully added"
                con.close()
        except:
            msg = "error in insert operation"
        return msg   

    def records(self, fileType, id=False):
        con = sqlite3.connect("AudioFiles.db")
        cur = con.cursor()
        if fileType =="Audio":
            if id:
                cur.execute(f"select * from {fileType} where id = {id}")
                row=cur.fetchall()
                return row
            else:
                cur.execute(f"select * from {fileType}")
                row=cur.fetchall()
                return row  
        elif fileType== "Podcast":
            if id:
                cur.execute(f"select * from {fileType} where id = {id}")
                row=cur.fetchall()
                return row
            else:
                cur.execute(f"select * from {fileType}")
                row=cur.fetchall()
                return row 
        elif fileType =="AudioBook":
            if id:
                cur.execute(f"select * from {fileType} where id = {id}")
                row=cur.fetchall()
                return row
            else:
                cur.execute(f"select * from {fileType}")
                row=cur.fetchall()
                return row 
        
    def UpdateRecords(self, fileType, col,val, id ):
        try:
            conn = sqlite3.connect('AudioFiles.db')
            cursor = conn.cursor()
            print("In record update")
            if fileType =="Audio":
                sql= f"UPDATE Audio SET {col} = {val} WHERE {col} = {id} ;"
                cursor.execute(sql)
                conn.commit()
            elif fileType== "Podcast":
                conn = sqlite3.connect('AudioFiles.db')
                cursor = conn.cursor()
                sql= f"UPDATE Podcast SET {col} = {val} WHERE {col} = { id } ;"
                cursor.execute(sql)
                conn.commit()
            elif fileType =="AudioBook":

                sql= f"UPDATE AudioBook SET {col} = {val} WHERE {col} = {id} ;"
                cursor.execute(sql)
                conn.commit()
           
        except Exception as e:

            return e
    
    def deleteRecords(self,fileType, id):
        if fileType =="Audio":
            sql = f"DELETE FROM {fileType} WHERE ID ={id}"
            conn = sqlite3.connect('AudioFiles.db')
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                conn.commit()
                return "Record deleted"
            except Exception as e:
                conn.rollback()
                return e
        elif fileType== "Podcast":
            sql = f"DELETE FROM {fileType} WHERE ID ={id}"
            conn = sqlite3.connect('AudioFiles.db')
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                conn.commit()
                return "Record deleted"
            except Exception as e:
                conn.rollback()
                return e
        elif fileType =="AudioBook":
            sql = f"DELETE FROM {fileType} WHERE ID ={id}"
            conn = sqlite3.connect('AudioFiles.db')
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                conn.commit()
                return "Record deleted"
            except Exception as e:
                conn.rollback()
                return e

        
