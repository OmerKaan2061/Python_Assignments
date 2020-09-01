number = input("Please enter a positive number :")
strong = len(number)
i = 0
summon = 0
if not number.isdigit() :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif float(number) < 0:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    while i < strong:
        digit = int(number[i]) ** strong
        summon += digit
        i +=1
    if summon == int(number):
        print(number, "is an armstrong number")
    else:
        print(number, "is not an armstrong number")