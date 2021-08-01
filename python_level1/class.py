class Unit:
    def __init__(self):
        print('unit 생성자')

class Flyable:
    def __init__(self):
        print('flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def  __init__(self):
        super().__init__()

dropship = FlyableUnit()