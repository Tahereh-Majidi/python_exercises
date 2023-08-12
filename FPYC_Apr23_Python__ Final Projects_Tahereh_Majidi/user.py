from person  import *
from book import *
from function import *
from datetime import datetime, timedelta
import datetime
class User(Person):
    def __init__(self,f_name,l_name,email,phone_number):
        Person.__init__(self,f_name,l_name)
        self.email=email
        self.phone_number=phone_number
        
    def get_all_info(self):
            print(f"The unique id of user is : {self.unique_id}")
            print(f"The  first name of user is: {self.first_name}")
            print(f"The last name of user  is: {self.last_name}")
            print(f"The eamil of user  is: {self.email}")   
            print(f"The phone number of user  is: {self.phone_number}")
            print("-"*50)  
    def borrow_books(self):
            x=datetime.now()
            t=datetime.now() + timedelta(days=10)
            print("Today's date for borrowing the books is: ")
            print(x.strftime("%Y"),x.strftime("%m"),x.strftime("%d"))
            print("The due date for returning the books is: ")
            print(t.strftime("%Y"),t.strftime("%m"),t.strftime("%d"))

    

                     
#if __name__== "__main__":                  

#=User("mohhamad amir","kherkhah","amir_1991@gmail.com","+6283840355905")
#obj3.availablebooks()



#u1=User("mohhamad amir","kherkhah","amir_1991@gmail.com","+6283840355905") 
#u1.get_all_info()  
#u1.personal_info()                       