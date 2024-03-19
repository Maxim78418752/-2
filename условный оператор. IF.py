x = 50
print('привет')
if x < 10:
    print('меньше нуля')
print("пока")

a, b = 20, 10
if a > b:
    print('a>b')
if a > b and a > 15:
    print('повезло')
if (a > b) and (a > 15 or b < 12):
    print('успех')
if 10 < b and b < 50:
    print('молодец')

if '23' > '123':
    print('excelent')
if '456' > '45':
    print('excelent')
if [1,1] > [2,2,2]:
    print('excelent')

if '6' > 5:                  #не работает
    print('excelent')
if [5,6] > 4:                #не работает
    print('excelent')
if '6' != 6:
    print('excelent')