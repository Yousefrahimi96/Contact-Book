class ContactBook:
    def __init__(self):
        self.contact = {}
        
    def add_contact(self, name, number, email):
        
        if name not in self.contact:
            self.contact[name] = {"number" : number, "email" : email}
        else:
            print("name is exist") 
        
    def detect_contact(self, name):
        if name in self.contact:
            return self.contact[name]
        else:
            print(f"{name} is not exist")
    
    def update_contact(self, name, number= None, email= None):
        if name in self.contact:
            if number is not None:
                self.contact[name]['number'] = number
            if email is not None:
                self.contact[name]['email'] = email
        else:
            print(f"{name} is not exist")
    
    def veiw_contact(self):
        for name, info in self.contact.items():
            print("Name:", name)
            print("Number:", info['number'])
            print("Email:", info['email'])
        
    def delete_contact(self, name):
        if name in self.contact:
            del self.contact[name]
            print(f"{name} succesfuly deleted")
        else:
            print(f"{name} not found")

