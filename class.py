class Students():
    name=""
    age=12
    grade=8
    def __init__(self):
        print("Write name")

    def details(self):
        self.name=input("What is your name")
        self.age=input("What is your age")
        self.grade=input("What grade are you in")
    def display(self):
        print(self.name)
        print(self.age)
        print(self.grade)
Arush=Students()
Arush.details()
Arush.display()
Tom=Students()
Tom.details()
