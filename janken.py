'''
Created on 2019/10/09

@author: t17cs041
'''

import random

print('1:グー, 2:チョキ, 3:パー')
p = False

while p == False:
    print('数字を1つ入力:')
    
    x = input()
    xx = int(x)
    y = random.randrange(1,4)
    print('相手の手:',y)
    
    if (xx == 1 and y == 2) or (xx == 2 and y == 3) or (xx == 3 and y == 1):
        print('あなたの勝ち')
        p = True
    elif (xx == 2 and y == 1) or (xx == 3 and y == 2) or (xx == 1 and y == 3):
        print('あなたの負け')
        p = True
    elif xx == y:
        print('あいこ')

    