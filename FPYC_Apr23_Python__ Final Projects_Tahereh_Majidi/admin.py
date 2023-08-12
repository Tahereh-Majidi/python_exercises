
from person  import *
class Admin (Person):
    def __init__(self,f_name,l_name,user_name,password):
        self.user_name=user_name
        self.password=password
        Person.__init__(self,f_name,l_name)
    def get_all_info(self):
            print(f"The unique id of admin is : {self.unique_id}")
            print(f"The  first name of admin is: {self.first_name}")
            print(f"The last name of admin  is: {self.last_name}")
            print(f"The user_name of admin  is: {self.user_name}")   
            print(f"The password of admin is: {self.password}")
            print("-"*50)

     
  
    def  log_in(self):
          
        userInput = input("What is your username?\n")

        if userInput == self.user_name:
            a=input("Password?\n")   
            if a == self.password:
                print("Welcome our admin!")
            else:
                print("That is the wrong password.")
        else:
            print("That is the wrong username.")
        
                   

#u1=Admin("ali","majidi","www.yahoo","0915148793") 
#u1.log_in()  
#u2=Admin ("sara","majidi","www.yahoo.com",98912148758) 
#u2.personal_info()                                   