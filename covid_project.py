while True:
    age = input('Are you a cigarette addict older than 75 years old? Yes/No :').title()

    if (age == "No" or age == "Yes"):
        break
    else:
        print("Please just enter Yes or No")        

while True:
    chronic = input('Do you have a severe chronic disease? Yes/No :').title()

    if (chronic == "No" or chronic == "Yes"):
        break
    else:
        print("Please just enter Yes or No")
        
while True:
    immuni = input('Is your immune system too weak? Yes/No :').title()

    if (immuni == "No" or immuni == "Yes"):
        break
    else:
        print("Please just enter Yes or No")
        

if age == 'No' and chronic == 'No' and immuni == 'No':
    print("You are not in risky group")
elif age == 'Yes' or chronic == 'Yes' and immuni == 'Yes':
    print("You are in risky group")