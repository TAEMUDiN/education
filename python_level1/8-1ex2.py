class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
try:
    chicken = 10
    waiting = 1
    while(True):
        print('[남은치킨 : {0}]'.format(chicken))
        order = int(input('치킨 몇 마리 주문 하십니까?'))
        if order > chicken:
            print('재료 부족')
        elif order == 0:
            raise ValueError
     
        
        else:
            print('[대기번호 {}]{} 마리 주문이 완료 되었습니다.'.format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError('입력값 : {0}'.format(order))

except ValueError:
    print('잘못된 값을 입력 하였습니다.')

except SoldOutError:
    print('재고가 소진되어 더 이상 주문 안됨')