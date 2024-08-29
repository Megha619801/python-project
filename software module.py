#Question from python module
#Q.no.1

size_limit=42
length_of_zander = int(input("Enter the length of the zander in centimeter: "))
if length_of_zander < size_limit:
    print("release the fish back into the lake")
    remain_length = size_limit - length_of_zander
    print(remain_length, 'centimeters will meet size limit')
else:
    print('the fish was caught')



#Q.no.2

cabin_class= (input(" enter the cabin class of a cruise ship"))

if cabin_class == "Lux":
    print(" upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
elif cabin_class == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")


#Q.no.3

normal_male_haemoglobin = '134-167'
normal_female_haemoglobin = '117-155'

biological_gender = input("enter the gender: ")
haemoglobin_value = input("enter the haemoglobin value: ")

if biological_gender == "male":
    if haemoglobin_value == normal_male_haemoglobin:
        print("normal")
    elif haemoglobin_value < normal_female_haemoglobin:
        print("low")
    else:
        print("high")

if biological_gender == "female":
    if haemoglobin_value == normal_female_haemoglobin:
        print("normal")
    elif haemoglobin_value < normal_female_haemoglobin:
        print("low")
    else:
        print("high")

#Q.no.4

year = int(input("enter the year: "))

if year%4==0:
    if year%100!=0 or year%400==0:
        print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

