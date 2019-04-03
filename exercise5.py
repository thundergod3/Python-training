#Part 1
list_quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
list_danso = [150300, 247100, 333300, 266800, 420900, 318000]

print(max(list_danso))
print(min(list_danso))

print(list_quan[0])
print(list_quan[4])

list_dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]

list_matdodanso = []

for i in range(len(list_danso)):
    matdodanso = list_danso[i]/list_dientich[i]   
    list_matdodanso.append(matdodanso) 
print(list_matdodanso)