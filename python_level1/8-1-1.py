class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성 되었습니다'.format(self.name))
        print('체력 {0}, 공격력{1}'.format(self.hp,self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit('탱크', 150, 35)

wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

wraith2 = Unit('빼앗은 레이스', 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print('{0}는 현재 클로킹 상태입니다.'.format(wraith2.name))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location):
        print('{0} : {1} 방향으로 적군을 공격 합니다.'.format(self.name, location, self.damage))

    # def damaged(self, damage):
    #     print('{0} : {1} 데미지를 입었습니다.'.format(self.name, self.damage)
    #     self.hp -= damage
    #     print('{0} : 현재 체력은 {1} 입니다'.format(self.name, self.hp))
    #     if self.hp <= 0:
    #         print('{0} : 파괴되었습니다.'.format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도{2}'.format(name, location, self.flying_speed))

class FlyableAttackUint(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.Fly(valkyrie.name,'3시')

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')