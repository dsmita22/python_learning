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

# car game
# If type
# help or HELP :
#    start - to Start the car
#    stop -to stop the car
#    quit - to exit
# if type any other text it should show
#     I don't understand

userInput = ""
started = False
while True:
    userInput = input(">").lower()
    if userInput == 'start':
        if started:
            print('Car already started')
        else:
            started=True
            print('Car started')
    elif userInput == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started=False
            print('Car stopped')
    elif userInput == 'help':
        print("""
start - to Start the car
stop -to stop the car
quit - to exit
        """)
    elif userInput == 'quit':
        break
    else:
        print("Sorry I don't understand that")

# For loop
# Print (0,0)(0,1)(0,2)(1,0)(1,1)....(3,0)..(3,2)

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# Print
# XXXXX
# XX
# XXXXX
# XX
# XX

numbers = [5, 2, 5, 2, 2]
for X_count in numbers:
    print('X' * X_count)

# Write a program to find largest number in the list
list = [10, 30, 10, 30, 20]
max = list[0]
for number in list:
    if number > max:
        max = number
print(max)

# print all matrix value
matrix =[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
for row in matrix:
     for item in row:
         print(item)

# remove duplicate number from list
List = [2, 2, 4, 5, 6, 7, 7, 9, 8]
unique=[]
for number in List:
    if number not in unique:
        unique.append(number)
print(unique)

# Exception
try:
    age = int(input("Age :"))
    print(age)
except:
    print('Invalid value')

# Class
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()