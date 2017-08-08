import time
class  CoffeeMachine:
    WATER_LEVEL = 100
    
    def _start_machine(self): #protected
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please add water ..")
            return False
        
    def __boil_water(self):  #private
        return "Boiling..."
        
    def make_coffee(self):
        if self._start_machine():
            self.WATER_LEVEL -= 50
            print(self.__boil_water())
            time.sleep(2)
            print("Coffee is ready my dear")


def main():
    machine = CoffeeMachine()

    print("Make coffee: Public", machine.make_coffee()) # ok
    print("Start machine: Protected", machine._start_machine()) # ok
    print("Boil water: Private", machine.__boil_water()) # pas ok
    # si on veut utiliser une méthode privée: _class__privateMethode()
    print("Boil water: Private", machine._CoffeeMachine__boil_water()) # pas ok


main()
