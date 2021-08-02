# try:
#     nums = []
#     nums.append
#     nums.append(int(input('첫번쨰 숫자를 입력하세요')))
#     nums.append(int(input('두번쨰 숫자를 입력하세요')))
#     # nums.append(int(nums[0]/nums[1])
#     print('{0}/{1}={2}'.format(nums[0],nums[1],nums[2]))

# except ValueError:
#     print('에러 발생')

# except ZeroDivisionError as err:
#     print(err)

# except Exception as err:
#     print('알 수 없는 에러!!')
#     print(err)

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫번째 숫자 '))
    num2 = int(input('두번째 숫자 '))
    if num1 >= 10 or num2 >= 10:
         raise BigNumberError('입력값 : {0},{1}'.format(num1,num2))
    print(('{0}/{1}={2}'.format(num1,num2,int(num1/num2))))

except ValueError:
    print('잘못된 값 입력')

except BigNumberError as err:
    print('잘못된 값 입력 한자리 수만 입력하세요')
    print(err)
finally:
    print('계산기 이용해 주셔서 감사'    )