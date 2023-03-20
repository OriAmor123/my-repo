class People:
    def __init__(self, name, age, mail, adress):
        self.name = name
        self.age = age
        self.mail = mail
        self.adress = adress
        if 6< self.age <18:
            self.grade = self.age - 6
        else:
            self.grade = 'Not in grade'
    
    def get_grade(self):
        if self.grade != None:
            return f'{self.name} is on grade {self.grade}'
        else:
            return f'{self.name} is not in grade'
    
    def view(self):
        view_dict = {
            'name': self.name,
            'age': self.age,
            'mail': self.mail,
            'adress': self.adress,
            'grade': self.grade
        }
        return view_dict
        

p1 = People('Ori', 19, 'Oriamor50@gmail.com', 'USA')
print(p1.view())