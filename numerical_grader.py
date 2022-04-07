# This program will allow a user to enter a numerical grade and get a letter grade

# the user will enter the earned numerical grade value
number = int(input("Enter your grade "))

if number >= 90:
    print("Congrats, you have received an A!")
elif 80 < number < 89:
    print("Congrats, you have received a B!")
elif 70 < number < 79:
    print('You have received a C!')
elif 60 < number < 69 :
    print('Did you even try? D')
else:
   print(" Your\'re kidding right? F ")