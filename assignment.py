#Question from python module 2 Q.no.(1)

name=input("what is your name?")
print("Hello,", name, '!')


#Q.no.2
radius = int(input("Enter the radius of the circle ? "))
area = 3.14 * radius**2
print("The area of the circle is:", area)


#Q.no.3
length=int(input("Enter the length of a rectangle"))
width= int(input("Enter the width of a rectangle"))
perimeter=2*length*width
area= length*width
print("The perimeter of the rectangle is:" , perimeter)
print("The area of the rectangle is:" , area)


#Q.no.4
num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))

sum = num1+num2+num3
product = num1*num2*num3
average=sum/3

print(f"The sum of 3 numbers: {sum}")
print(f"The product of 3 numbers: {product}")
print(f"The average of 3 numbers: {average:.2f}")

#Q.no.5
talent=float(input("Enter the Talent: "))
pounds=float(input("Enter the Pounds: "))
lots= float(input("Enter the Lots: "))

lot_to_grams = 13.3
pound_to_lots = 32
talent_to_pounds = 20
total_lots = (talent * talent_to_pounds * pound_to_lots) + (pounds * pound_to_lots) + lots
total_grams = (total_lots * lot_to_grams)

kilograms = total_grams//1000
grams= total_grams%1000

print(f"The weight in modern units :  , {kilograms} kilograms and {grams:.2f} grams.")


#Q.no.6

import random

three_digit_one= str(random.randint(0,9))
three_digit_two= str(random.randint(0,9))
three_digit_three= str(random.randint(0,9))

three_digit_code= three_digit_one+three_digit_two+three_digit_three
print('3 digit code: ' + three_digit_code)

four_digit_one= str(random.randint(1,6))
four_digit_two= str(random.randint(1,6))
four_digit_three= str(random.randint(1,6))
four_digit_four= str(random.randint(1,6))

four_digit_code= four_digit_one+four_digit_two+four_digit_three+four_digit_four
print('4 digit code: ' + four_digit_code)




