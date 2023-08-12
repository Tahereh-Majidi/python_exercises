from admin import *
from book import *
from user import *
from function import *

#creat obj1
obj1=Library()
#creat obj2 
#[("Steve","Jobs","Steve_Job","123456"),("Marie","Curie","Marie_Curie","123456"),("Mark","Zuckerberg","Mark_Zuckerberg","123456")]
obj2=Admin("Steve","Jobs","Steve_Job","123456") 
userInput = input("What is your username?\n")
if userInput == obj2.user_name:
    a=input("Password?\n")   
    if a == obj2.password:
        print("Welcome our admin!")
    

        while True:
                admin=input("Please select an option:   add/remove/edit/search/display/borrow/adduser/exit :   ")
                admin=admin.lower()
                if admin=="add":
                        name=input("Enter name of your book: ")
                        author=input("Enter author of your book: ")
                        language=input("Enter language of your book: ")
                        field=input("Enter field of your book: ")
                        publication_date=input("Enter publication_date of your book: ")
                        obj1.add_book(name,author,language,field,publication_date)
                        print("Added")
                elif admin=="display":
                    obj1.display()   
                elif admin=="edit":
                    id=input("Enter a id to edit: ")
                    obj1.edit(id)
                elif admin=="remove":
                    id=input("Enter a id to remove: ")
                    obj1.remove(id)
                    print(f"removed {id}")
                elif admin=="search":
                    name = input("name of your contact: ")
                    results =obj1.search(name)
                    for unique_id, name,author,language,field,publication_date in results:
                        print(f"{unique_id}: {name}--->{author}--->{language}--->{field}--->{publication_date}")
                elif admin=="borrowbook":
                        bookname=input("Enter name of the book to borrowing: ") 
                        obj1.borrowbook(bookname) 
                elif admin=="adduser":
                     obj1.add_user()  
                     print("ADDED USER")        
                elif admin=="borrow":
                     id_book=input("Enter id_book for borrowing the books: ")
                     id_user=input("Enter id_user for borrowing the books: ")
                     id_admin=input("Enter id_admin for borrowing the books: ")
                     date_borrow=input("Enter today's date for borrowing the books: ")
                     date_return=input("Enter the due date for returning the books: ")
                     obj1.borrow_book(id_book, id_user,id_admin ,date_borrow, date_return)
                     print("Added user")      
                elif admin=="":
                        pass
                elif admin=="exit":
                        break
                else:
                        print(f"{admin}: command not found!")
    else:
        print("That is the wrong password.")
else:
     print("That is the wrong username.")
     while True:
        user=input("Please select an option:   select/availablebooks/exit :   ")
        user=user.lower()
        if user=="select":
             name=input("Enter name of the book: ")
             obj1.select_book(name)
             print("You have successfully borrowed")
        elif user=="availablebooks":
            obj1.availablebooks()  
        elif user=="":
             pass
        elif user=="exit":
             break
        else:
             print(f"{user}: command not found!")
    
   
    
        