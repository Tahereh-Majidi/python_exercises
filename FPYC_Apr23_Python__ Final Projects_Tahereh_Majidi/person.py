import uuid
class Person:
        def __init__(self,f_name,l_name):
            self.unique_id=str(uuid.uuid4())[0:5]
            self.first_name=f_name
            self.last_name=l_name
        def personal_info(self):
            print(f"The unique id of admin is : {self.unique_id}")
            print(f"The  first name of admin is: {self.first_name}")
            print(f"The last name of admin  is: {self.last_name}")    
