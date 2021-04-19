#!/usr/bin/env python3
"""
   bahuanghou
   2021 pratice by h
"""

qipan=[-1 for i in range(8)]
total = 0
def judge(rows):
    global qipan
    for i in range(rows):
        if qipan[i]==qipan[rows]:
            return False
        if (rows-i)*(rows-i) == (qipan[i]-qipan[rows])*(qipan[i]-qipan[rows]):
            return False
    return True

def printqipan():
    global qipan
    for i in range(8):
        for j in range(8):
            if qipan[i]==j:
                print('Q',end=' ')
            else:
                print('*',end=' ')
        print('\r')
		
def findqueen(row):
    global qipan,total
    if row>7:
        total = total + 1
        print("第{}种放置的方法".format(total))
        printqipan()
		
    else:
        for i in range(8):
            qipan[row]=i
            if judge(row):
                findqueen(row+1)


findqueen(0)	