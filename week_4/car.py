class car:
    def __init__(self,model,make,year_of_manufacture,engine_capacity):
        self.model = model
        self.make = make
        self.year= year_of_manufacture
        self.engine_capacity=engine_capacity

    def get_model(self):
        return self.model
    def get_make(self):
        return self.make
    def get_year(self):
        return self.year_of_manufacture
    def get_engine_capacity(self):
        return self.engine_capacity
    
    #setters-used to set attributes
    def set_model(self,model):
        self.model=model
    def set_make(self,make):
        self.make=make
    def set_year_of_manufacture(self,year_of_manufacture):
        self.year_of_manufacture=year_of_manufacture





car1= car("demio","nissan",2018,1300)
car2= car("mazda","toyota",2020,1500)
car3= car("hilux","toyota",2015,1780)

car2.set_year_of_manufacture(2023)
car3.set_year_of_manufacture(2021)


print(car1.get_model())
print(car1.get_make())
print(car1.get_year_of_manufacture())
print(car1.get_engine_capacity)

print(car2.get_model())
print(car2.get_make())
print(car2.get_year())
print(car2.get_engine_capacity)

print(car3.get_model())
print(car3.get_make())
print(car3.get_year)
print(car3.get_engine_capacity)