# import models
from itertools import cycle
# input range
maximum = input('Please enter the maximum: ')
try:
    # find perfect numbers
    def perfect(num):
        if (str(num)[-1] == '6' or str(num)[-2:len(str(num))] == '28') and num != 0 and ((num%3==1 and num%9==1 and '1' in str(num%27)) or num==6):
            # Can't use num%27==0 because 496%27==10.
            factor_sum = 0
            for counter in range(1,num):
                if num % counter == 0:
                    factor_sum += counter
            if factor_sum == num:
                return num
            else:
                return False
        else:
            return False
    number = 0
    count = 1
    if maximum == 'Infinity' or maximum == '8)' or maximum == '∞':  # "8)" means "tipped 8", which is "∞"。
        while True:
            try:
                perfectTF = perfect(number)
                if perfectTF != False:
                    print(str(perfectTF)+' is a perfect number!')
                number += count
                count += 1
            except KeyboardInterrupt:
                print('Exited. Thanks for using!')
                break
    else:
        while number< int(maximum)+1:
            if perfect(number) != False:
                print(str(perfect(number))+' is a perfect number!')
            number += count
            count += 1
        print('Ended. Thanks for using!')
except StopIteration: pass
except: print('Unexpected Error: '); raise
