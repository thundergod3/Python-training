number_input = int(input('Ban thich con so nao ?'))

if number_input < 5:
    for i in range(5, (number_input - 1), -1):
        print(i)
else:
    for i in range(5, (number_input + 1)):
        print(i)

for j in range(20, 9, -1):
    print(j)

n = int(input('Nhap so dau ='))
m = int(input('Nhap so thu hai ='))

if n < m:
    print('Nhap lai 2 so sao cho so dau lon hon so hai')
else:
    for k in range(n, (m-1), -1):
        print(k)

print('How many leg does a spider have?')
print('1. None')
print('2. 4 legs')
print('3. 8 legs')
print('4. 12 legs')

answer_input = input('Your answer ?')
while True:
    if (answer_input == '1') or (answer_input == '2') or (answer_input == '3') or (answer_input == '4'):
        if (answer_input == '3'):
            print('You answer right')
            break
        else:
            print('Wrong answer, the answer is 3: 8 legs')
            break
    else:
        print('The answer must me 1, 2, 3 or 4')
        new_input = input('enter again:')
        if (new_input == '1') or (new_input == '2') or (new_input == '3') or (new_input == '4'):
            if (new_input == '3'):
                print('You answer right')
                break
            else:
                print('Wrong answer, the answer is 3: 8 legs')
                break
