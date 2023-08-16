# class Human:
#     def __init__(self,name,height,weight) -> None:
#         self.name = name
#         self.height = height
#         self.weight = weight


# class Basketball_Player(Human):
#     def __init__(self,name,height,weight,rating) -> None:
#         super().__init__(name,height,weight)
#         self.rating = rating
    
#     @property
#     def shoot(self):
#         print("He shoots the ball")
#         if self.rating > 3:
#             return("He makes the shot")
#         else:
#             return("He doesn't make the shot")


# oplayer = Basketball_Player("Kobe",6.6,180,4.1)
# print(oplayer.shoot)class Human:
#     def __init__(self,name,height,weight) -> None:
#         self.name = name
#         self.height = height
#         self.weight = weight


# class Basketball_Player(Human):
#     def __init__(self,name,height,weight,rating) -> None:
#         super().__init__(name,height,weight)
#         self.rating = rating
    
#     @property
#     def shoot(self):
#         print("He shoots the ball")
#         if self.rating > 3:
#             return("He makes the shot")
#         else:
#             return("He doesn't make the shot")


# oplayer = Basketball_Player("Kobe",6.6,180,4.1)
# print(oplayer.shoot)class Human:
#     def __init__(self,name,height,weight) -> None:
#         self.name = name
#         self.height = height
#         self.weight = weight


# class Basketball_Player(Human):
#     def __init__(self,name,height,weight,rating) -> None:
#         super().__init__(name,height,weight)
#         self.rating = rating
    
#     @property
#     def shoot(self):
#         print("He shoots the ball")
#         if self.rating > 3:
#             return("He makes the shot")
#         else:
#             return("He doesn't make the shot")


# oplayer = Basketball_Player("Kobe",6.6,180,4.1)
# print(oplayer.shoot)

class Fan:
    def __init__(self) -> None:
        self.on = False
        self.speed = 0
    
    @property
    def turn_on(self):
        self.on = True
    
    @property
    def turn_off(self):
        self.on = False
    
    @property
    def increase_speed(self):
        if self.speed < 5 and self.on == True:
            self.speed += 1

    @property
    def decrease_speed(self):
        if self.speed >0 and self.on == True:
            self.speed -= 1

    @property
    def show(self):
        return(f"Fan On:{self.on}\t Fan speed:{self.speed}")

ofan = Fan()
print(ofan.show)
ofan.increase_speed
ofan.increase_speed
ofan.turn_on
ofan.increase_speed
ofan.increase_speed
print(ofan.show)
