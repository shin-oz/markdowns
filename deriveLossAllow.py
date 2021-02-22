import numpy as np
import math

def deriveLossAllow():
    # 送信パケット数
    # n = 105000
    n = int(input())
    # 許容パケットロス数
    N = 1
    # 信頼区間
    p = 0.95
    # ロス目標
    criteria_loss = pow(10, -3) # 1E-3
    # print(criteria_loss)

    # 許容パケットロス数導出式右辺の第二項で使うシグマについて
    array = list()
    # 0~N-1の和になるため注意 
    for i in range(N + 1):
        k = i
        # print(i)
        array.append( pow((n * criteria_loss), k) / math.factorial(k))

    # print(array)
    # print(np.sum(array))

    # 右辺のみを見ればできるのでは？←左辺の式は常に固定
    # N = - np.log( 1 - p ) / criteria_loss + sigma / criteria_loss
    secondNum = np.log(np.sum(array)) / criteria_loss
    print(secondNum)
    print(- np.log( 1 - p) / criteria_loss)
    result = - np.log( 1 - p ) / criteria_loss + secondNum
    print("result: ", result)
    print("n: ", n)


    #  N = 0 n = 2995
    #  N = 1 n = 4743
    #  N = 50 n = 4743

deriveLossAllow()