print('Smita')
print('*' * 10)

#Defind veriable
price = 10
print('ex 1 :', price)

#update value of veriable
price = 10
price = 20
print('ex 2 :', price)

# We check in a patient named John Smith.He's 20 trs old and is a new patient
patient_name = 'JOhn Smith'
patient_age = 20
is_new = True

#take the input and print
name = input('What is your name? ')
print('Hi ' + name)

#ask 2 question: person's name and fav colour, then print message like 'Smita likes blue'
name1 = input('what is your name? ')
colour = input('what is your favourite colour? ')
print(name1+' likes '+colour)

#ask a user their weight (in pound) then convert it to kilograms and print on terminal
weight_lbs = input('what is your weight? ')
print(type(weight_lbs))
weight_kg = int(weight_lbs) * 0.45
print(type(weight_kg))
print('Weight in KG ' + str(weight_kg))

# String methods
course ='Python learning'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('learning', 'learning project'))
print('Python' in course)

# condition
# Ques: if it's hot
#             It's a hot day
#             Drink plenty of water
#       otherwise if it's cold
#             It's a cold day
#             Wear warm clothes
#       otherwise
#             It's a lovely day
is_hot = False
is_cold = True
if is_hot:
     print("It's hot day")
     print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print('Enjoy your day')

# Logical operator
# if applicant has hign income AND good credit
#      Eligible for loan
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit :
     print("Eligible for loan")

# if applicant has hign income OR good credit
#      Eligible for loan
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit :
     print("Eligible for loan")

# While Loop
i=1
while i<=5:
    print('*' * i)
    i=i+1
print("DONE")

# Guess the secret number using while loop
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count<guess_limit  :
    guess = int(input("Guess : "))
    guess_count += 1
    if guess == secret_number :
        print("you won")
        break
else:
    print("sorry you fail to guess")