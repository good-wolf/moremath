import math
from Dice import Dice

first_nums = [] 
symbols = []
second_nums = []
answers = []
all_symbols = [1,2,3,4]
x = 0


print('------欢迎使用moremath1.0.0------')
print('------反馈：wonderful.liu2008@outlook.com------')
print('------可以通过邮箱获得使用指南------')

def prime (num):
    if num < 2:
        return False
    i = 2
    while i < math.sprt(num):
        if num % i == 0:
            return False
        i += 1
    return True

def long_count(first_num,symbol,second_num):
    first_nums = first_num
    symbols = symbol
    second_nums = second_num
    if len(first_nums) == len(symbols) and len(symbol) == len(second_nums):
        for i in range(len(symbols)):
            if symbols[i] == '+':
                answers.append(first_nums[i] + second_nums[i])
            elif symbols[i] == '-':
                answers.append(first_nums[i] - second_nums[i])
            elif symbols[i] == '*':
                answers.append(first_nums[i] * second_nums[i])
            elif symbols[i] == '/':
                answers.append(first_nums[i] / second_nums[i])
            else:
                return '输入错误'

        answer = 0
        for x in answers:
            answer += x
        return answer
    else:
        first_nums = []
        symbols = []
        second_nums = []
        print('输入错误')

def fermat_number_finder(max_n,min_n = 1):
    for num in range(min_n,max_n):
        fermat_num = 2 ** num ** 2
        fermat_nums.append(fermat_num)

def play_dice(name,time,faces = 6,scores = [1,2,3,4,5,6],visualization = True):
    name = Dice(time,faces,scores,visualization)
    name.start()

def times_table():
    for m in range(1, 10):
        for n in range(1, m+1):
            print('%s × %s = %s' % (m, n, m*n), end=' ')
        print()

times_table()
