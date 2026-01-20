class Car():
    
        
    def acceleration(self):
        self.speed=self.speed+10
    def details(self):
        self.brand=input("What is your car's brand ")
        self.speed=int(input("What is your car's speed "))
    
        

    def display(self):
        print(self.brand)
        print(self.speed)
    
        

i=Car()
i.details()
i.acceleration()
i.acceleration()
i.display()
