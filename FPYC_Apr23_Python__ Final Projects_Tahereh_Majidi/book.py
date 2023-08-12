import uuid
class Book :
    def __init__(self,name,author,language,field,publication_date):
        self.unique_id=str(uuid.uuid4())[0:5]
        self.name=name
        self.author=author
        self.language=language
        self.field=field
        self.publication_date=publication_date
        
      
    
    def get_all_info(self):
            print(f"The unique id of book is : {self.unique_id}")
            print(f"The name of book  is: {self.name}")
            print(f"The author of book  is: {self.author}")
            print(f"The language of book  is: {self.language}")   
            print(f"The field of book  is: {self.field}")
            print(f"The publication date of book is : {self.publication_date}")
            print("-"*50)  

    def get_name(self):   
        print(f"name of book: {self.name}")        