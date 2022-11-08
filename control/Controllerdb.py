from tkinter import messagebox
import mysql.connector as mysql
from mysql.connector import Error
class controller:
    
   def getConnection(self):
        try:
           con = mysql.connect(host='localhost', database='booking', user='root', password='')
           return con
        except Error as err:
            print(err.msg)
        except:
            messagebox.showerror('Database Error', 'Unable to connect to Database')
    
    #inserting into database
   def queryDB(self,query,values=''):
       con= self.getConnection()
       cursor = con.cursor()
       cursor.execute(query,values)
       con.commit()
       con.close()
   
   #closing connection 
   def closeConnection(self):
      con= self.getConnection()
      con.close()
      
   def getLogin(self,query,values):
        try:
            con =self.getConnection()
            cursor = con.cursor()
            cursor.execute(query,values)
            row=cursor.fetchone()
            return row
        except:
           print('Error Occur')
        finally:
           con.close()

      
#    def clearbtn(self,values):
#        self.values=values
#        values.set("")