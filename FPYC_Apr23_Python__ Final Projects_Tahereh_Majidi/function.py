from book import *
from config import *
class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,name,author,language,field,publication_date):
      
        mycursor = mydb.cursor()
        query = "INSERT INTO Books_all (name,author,language,field,publication_date,is_available) VALUES (%s,%s,%s,%s,%s,%s)"
        values =  (name,author,language,field,publication_date,True)
        mycursor.execute(query, values)
        mydb.commit()
        mycursor.close()

    def add_user(self):
        mycursor = mydb.cursor()
        query = "INSERT INTO Users (first_name,last_name,email,phone_number) VALUES (%s,%s,%s,%s)"
        values = [("John","Smith","JohnSmith@gamil.com","+6233225588"),("Emily","Brown","EmilyBrown@yahoo.com","+1964589248"),("Thomas","Davis","ThomasDavis@gmail.com","+19987522"),
                  ("Victoria","Miller","VictoriaMiller@gmail.com","+8648972359"),("Jennifer","Taylor","JenniferTaylor@gmail.com","+6299785642")]
        mycursor.executemany(query, values)
        mydb.commit()
        mycursor.close()
           

    def display(self):
        mycursor = mydb.cursor()
        query = "SELECT * FROM Books_all"
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()

        if result:
          print("List of books:")
          for row in result:
              print(f"{row[0]}: {row[1]},{row[2]}, {row[3]}, {row[4]}, published in {row[5]}")
        else:
            print("No books found.")
    def edit(self,id):
            mycursor = mydb.cursor()
            query = "SELECT * FROM Books_all WHERE unique_id = %s"
            values=(id,)
            mycursor.execute(query,values)
            result = mycursor.fetchall()
          
            if result:
                new_info = input("Enter new information for the book (name, author, language, field, publication_date): ")
                info = new_info.split(",")
                query = "UPDATE Books1 SET name = %s, author = %s, language = %s, field = %s, publication_date = %s WHERE unique_id = %s"
                values = (info[0], info[1], info[2], info[3], int(info[4]), id)
                mycursor.execute(query,values)
                mydb.commit()
            else:
                print("Book not found") 
            mycursor.close()          

    def remove(self,id): 
        mycursor = mydb.cursor()
        query = "DELETE FROM Books_all WHERE unique_id = %s"
        values = (id, )
        mycursor.execute(query, values)
        mydb.commit()
        mycursor.close()                   


    def search(self, name):
        mycursor = mydb.cursor()
        query = "SELECT * FROM Books_all WHERE name LIKE %s"
        name = "%" + name + "%"
        values = (name,)
        mycursor.execute(query, values)
        Books1 = mycursor.fetchall()
        mycursor.close()
        return Books1
         
    
          

    def availablebooks(self):
        mycursor = mydb.cursor()
        query = "SELECT * FROM Books_all"
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()

        if result:
          print("List of books:")
          for row in result:
              print(f"{row[0]}: name: {row[1]}-->author: {row[2]}-->language: {row[3]}-->field: {row[4]}-->publication_date:{row[5]}--->is_available:{row[6]}")
        else:
            print("No books found.")

    def borrow_book(self,id_book, id_user,id_admin ,date_borrow, date_return):
        mycursor = mydb.cursor()
        query = "INSERT INTO  borrow_all (id_book, id_user,id_admin ,date_borrow, date_return) VALUES (%s, %s, %s, %s,%s)"
        values = (id_book, id_user,id_admin ,date_borrow, date_return)
        mycursor.execute(query, values)
        mydb.commit()
        mycursor.close()    

    def select_book(self,name):       
        mycursor = mydb.cursor()
        query ="UPDATE Books_all SET is_available = False WHERE name = %s"
        values= (name,)
        mycursor.execute(query,values)
        result = mycursor.fetchall()
        mycursor.close()
        
       