class Car:
    def __init__(self, brand, model, color, max_speed, fuel_capacity):
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        self.speed = 0
        self.is_started = False
        
    def honk(self):
        print(f"{self.brand}{self.model}: Beep Beep!")
        
    def start(self):
        if self.is_started: 
            print(f"{self.brand}{self.model} is already started!")
            
        else:
            self.is_started = True
            print(f"{self.brand}{self.model} has started!")
            
    def stop(self):
        if not self.is_started:
            print(f"{self.brand}{self.model} is already stopped!")
        
        else:
            self.is_started = False
            self.speed = 0
            print(f"{self.brand}{self.model} has stopped!")
            
    def accelerate(self, incerement):
        if not self.is_started :
            print("Please start the car first!")
            return
        
        if self.fuel_level <= 0:
            print("Not enough fuel! Please refuel")
            return
        
        self.speed += incerement
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        self.fuel_level -= incerement * 0.1
        if self.fuel_level < 0:
            self.fuel_level = 0
            
        print(f"Current speed: {self.speed} km/h | Fuel left : {self.fuel_level} liters")
        
    def brake (self, decrement):
        if self.speed <= 0:
            print("The car is already stationary.")
            
        else:
            self.speed -= decrement
            if self.speed < 0:
                self.speed = 0
            print(f"Current speed : {self.speed} km/h")
            
    def refuel(self, fuel_amount):
        if fuel_amount <= 0:
            print("Invalid fuel amount entered!")
            return
        self.fuel_level += fuel_amount
        if self.fuel_level > self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
        print(f"Refueling complete! Current fuel level: {self.fuel_level} liters")
            
            
    def info(self):
        print(f"""
              Car Information:
              -Brand : {self.brand}
              -Model : {self.model}
              -Color : {self.color}
              -Maximum Speed : {self.max_speed}
              -Fuel Tank Capacity : {self.fuel_capacity}
              -Current Fuel Level : {self.fuel_level}
              -Status : {"Started" if self.is_started else "Stopped"}
              """)      
        
#test example       
my_car = Car("Toyota ", "Corolla", "White", 180, 50)

my_car.honk()
my_car.start()
my_car.stop()
my_car.start()
my_car.accelerate(60)
my_car.brake(10)
my_car.refuel(5)
my_car.info()



        