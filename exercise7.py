import random 

number_1 = random.randrange(0, 20, 1)
number_2 = random.randrange(0, 20, 1)
result = number_1 + number_2
result_false = result + random.randrange(-3, 3, 1)
print(number_1, '+', number_2, '=', result_false)
flag = result == result_false

while True:
    answer = input('Answer:').lower()
    if (answer == 't'):
        checking = True
        if flag == checking:
            print('You right')
            break
        else: 
            print('You wrong')
            break
    if (answer == 'f'):
        checking = False
        if (flag == checking):
            print('You right')
            break
        else:
            print('You wrong')
            break
