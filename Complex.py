a = int(input('Please Enter Real Number " a " in  "a + ib" Formula= '))
b = int(input('Please Enter Imaginary number " b " in  "a + ib" Formula= '))
c = int(input('Please Enter Real Number" c " in  "c + id" Formula= '))
d = int(input('Please Enter Imaginary number" d " in  "c + id" Formula=  '))

Complex_Number1 = {'r' : a , 'i' : b}
Complex_Number2 = {'r' : c , 'i' : d}

def sum_complex(sum1 , sum2):
    result_sum = {}
    result_sum['r'] = sum1['r'] +sum2['r']
    result_sum['i'] = sum1['i'] + sum2['i']
    print(result_sum['r'] , '+' , result_sum['i'] , 'i')

def mul_complex(mul1 , mul2):
    result_mul = {}
    result_mul['r'] = mul1['r'] * mul2['r'] - mul1['i'] * mul2['i']
    result_mul['i'] = mul1['r'] * mul2['i'] + mul1['i'] * mul2['r']
    print(result_mul['r'] , '+' , result_mul['i'] , 'i')

def minus_complex(min1 , min2):
    result_mimus = {}
    result_mimus['r'] = min1['r'] + -1 * min2['r']
    result_mimus['i'] = min1['i'] + -1 * min2['i']
    print(result_mimus['r'] , '+' , result_mimus['i'] , 'i')


while True:
    print('1- Sum')
    print('2- Multiply')
    print('3-Minus ')
    print('4- exit')
    choice = int(input('Choose which one: '))
    if choice == 1:
        result = sum_complex(Complex_Number1 , Complex_Number2)
        
    elif choice == 2:
        result = mul_complex(Complex_Number1 , Complex_Number2)
        
    elif choice == 3:
        result = minus_complex(Complex_Number1 , Complex_Number2)
        
    elif choice == 4:
        break
print(result)   