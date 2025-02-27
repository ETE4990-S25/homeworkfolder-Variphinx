import json

class Person(object):
    
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.email = email

    def Save(self):
        with open('SavedData.json', w) as f:
            json.dump({"first_name" : self.name, "age" : self.age, "email" : self.email})

    def LoadSave(self):
        with open('SaveData.json') as f:
            return f.read()





class Student(Person):
    
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def Save(self):                                       ##Overwrite Save function to include ID
        with open('SavedData.json', w) as f:
            f.write({"first_name" : self.name, "age" : self.age, "email" : self.email, "student_id" : self.st})
