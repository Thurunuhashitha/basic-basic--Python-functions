#I. Receive a number and return its absolute value.
def absolute(a):
    if a < 0:
        return -a
    else:
        return a
x = float(input("Please enter a number: "))
value=absolute(x)
print("Absolute value is: ",value)

#II. Receive a number and return its sign in native form.
def sign(x):
    if x < 0:
        return "Sign of your Number is negative" 
    elif x > 0:
        return "Sign of your Number is positive" 
    else:
        return "Warning! You have entered zero"
a = float(input("Please input your number: "))
result = sign(a)
print(result)

#III. Receive a lowercase character and return its upper case.
while True:
    def upper_case(c):
    simple="qwertyuiopasdfghjklzxcvbnm"
    capital="QWERTYUIOPASDFGHJKLZXCVBNM"
    length=0
    count=0
    for i in c:
        length +=1 
        if length > 1:
            break
        valid = (c in simple) and length == 1 if not valid:
        return "Invalid character or unavailable length! try again"
        for i in simple:
            if c == i:
                return f'Upper case of {c} ->{capital[count]}' count += 1
                c = input("Enter the letter: ")
                uc = upper_case(c)
                print(uc+"\n")


#IV. Receive a number and return its cube (to the power 3).
def cube(num):
    return num * num * num
number = float(input("Please Enter any number : "))
d = cube(number)
print(f"The Cube of a Given Number {number} is = {d}")


#V. Receive two numbers and return their product.
def product(x):
    return x
number1 = float(input(" Enter the first number :\t"))
number2 = float(input(" Enter the second number :\t"))
a = product(number1*number2)
print(f" Product of {number1} x {number2} is =",a)


#VI. Receive three numbers and return the largest.
def largest_num(A1,A2,A3):
    if A1 > A2:
        if A1 > A3:
            return A1
        else:
            return A3
    else:
        if A2 > A3:
            return A2
        else:
            return A3
A1 = float(input("Enter the first number :"))
A2 = float(input("Enter the second number :"))
A3 = float(input("Enter the third number :"))
print(f"Largest number is \t:{largest_num(A1,A2,A3)}")

#VII. Receive a two digit number and return the message ‘Mono Digit’ if it is a mono digit number.
def mono_digit(num):
    if num[0] == num[1]:
        return "'Mono Digit' number"
    else:
        return "Not a Mono Digit Number"
num = int(input("Enter a two digit number: "))
num = str(num)
length = 0
for i in num:
    length += 1
    if length == 2:
        print(f"Number is {mono_digit(num)}")
    else:
        print("Input is not a two digit number")


#VIII. Receive three numbers and return their average.
def average(num1,num2,num3):
    return num1+num2+num3/3
    num1 = float(input("Enter The First Number :"))
    num2 = float(input("Enter The Second Number :"))
    num3 = float(input("Enter The Third Number :"))
    avg = average(num1,num2,num3)
    print(f"Average of the Given Numbers is:\n%.2f"%avg)


#IX. Receive an integer and return the sum of digits
def sum_of_digit(x):
    summ = 0
    for i in x:
        summ += int(i)
        return summ
    x = input("Enetr The Number : ")
    x = str(x)
    print(f"Sum Of Digit is :{sum_of_digit(x)}")

