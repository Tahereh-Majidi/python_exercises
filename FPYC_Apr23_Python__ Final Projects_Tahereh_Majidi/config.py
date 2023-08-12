import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tahere1369"
)
mycursor = mydb.cursor()
sql = "CREATE DATABASE main_pro"
try:
 mycursor.execute(sql)
except:
 print("DATABASE Exit")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tahere1369",
    database = "main_pro"
)
mycursor = mydb.cursor()

##########creat table book
sql1= """
        CREATE TABLE Books_all(
        unique_id int NOT NULL auto_increment,
        name varchar(255) NOT NULL,
        author varchar(255)NOT NULL,
        language varchar(255) NOT NULL,
        field varchar(255) NOT NULL,
        publication_date int NOT NULL,
        is_available BOOLEAN,
        PRIMARY KEY (unique_id)
        );
    """
try:
 mycursor.execute(sql1)
except:
  print("Table Exit")
################creat table admin
sql2="""
        CREATE TABLE Admin_all(
        unique_id int NOT NULL auto_increment,
        first_name varchar(255) NOT NULL,
        last_name varchar(255)NOT NULL,
        user_name varchar(255) NOT NULL,
        password varchar(255) NOT NULL,
        PRIMARY KEY (unique_id)
        );
    """
try:
 mycursor.execute(sql2)
except:
  print("Table Exit")
###############creat table user############
sql3="""
        CREATE TABLE Users(
        unique_id int NOT NULL auto_increment,
        first_name varchar(255) NOT NULL,
        last_name varchar(255)NOT NULL,
        email varchar(255) NOT NULL,
        phone_number varchar(255) NOT NULL,
        PRIMARY KEY (unique_id)
        );
    """
try:
 mycursor.execute(sql3)
except:
  print("Table Exit")

###############creat pivot  table############
sql4="""
        CREATE TABLE borrow_all(
        id int NOT NULL auto_increment,
        id_book int NOT NULL,
        id_user int NOT NULL,
        id_admin int NOT NULL,
        date_borrow varchar(255) NOT NULL,
        date_return varchar(255) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (id_book) REFERENCES Books_all(unique_id),
        FOREIGN KEY (id_user) REFERENCES Users (unique_id),
        FOREIGN KEY (id_admin) REFERENCES Admin_all (unique_id)
        );
    """
try:
 mycursor.execute(sql4)
except:
  print("Table Exit")  

#---------------------------add admins----------------------------------  
#mycursor = mydb.cursor()
#query = "INSERT INTO Admins_all (first_name, last_name,user_name, password) VALUES (%s,%s,%s,%s)"
#values = [("Steve","Jobs","Steve_Job","123456"),("Marie","Curie","Marie_Curie","123456"),("Mark","Zuckerberg","Mark_Zuckerberg","123456")]
#mycursor.executemany(query, values)
#mydb.commit()
#mycursor.close()


  

