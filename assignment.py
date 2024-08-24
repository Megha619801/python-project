#Question from python module 1 Q.no.(1)a
name="Mahi!"
print("Hello,", name)


#Q.no.2(a)
name=input("what is your name?")
print("Hello,", name, '!')


#Q.no.2(b)
radius = int(input("Enter the radius of the circle ? "))
area = 3.14 * radius**2
print("The area of the circle is:", area)


#Q.no.2(c)
length=int(input("Enter the length of a rectangle"))
width= int(input("Enter the width of a rectangle"))
perimeter=2*length*width
area= length*width
print("The perimeter of the rectangle is:" , perimeter)
print("The area of the rectangle is:" , area)


#Q.no.2(d)
num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
num3=int(input("Enter the number: "))

sum = num1+num2+num3
product = num1*num2*num3
average=sum/3

print(f"The sum of 3 numbers: {sum}")
print(f"The product of 3 numbers: {product}")
print(f"The average of 3 numbers: {average:.2f}")

#Q.no.2(e)
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


