# class Airplane:
# 	def __init__(self,make,model,year,max_speed,odometer,is_flying)
class Airplane:
    def __init__(self):
        self.make = 'Airbus'
        self.model = 'A380'
        self.year = 2007
        self.max_speed = 1020
        self.odometer = 57
        self.is_flying = False
        self.spatium = 567

    def take_off(self):
        self.is_flying = True
        return(self.is_flying)

    def fly(self, spatium):
        if self.is_flying:
            return(self.odometer + self.spatium)

    def land(self):
        self.is_flying = False
        return(self.is_flying)


airbus = Airplane()
print(airbus.take_off())
print(airbus.fly(3000))
print(airbus.land())

