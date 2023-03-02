#############
### DAY 1 ###
#############

# INPUT FUNCTION

name = input("whats your name?\n")
nameLength = len(name)
print(nameLength)

# VARIABLES

a = input("a: ")
b = input("b: ")

c = a 
a = b 
b = c 

print("a: " + a)
print("b: " + b)

#BAND NAME GENERATOR

print("Welcome to the Band Name Generator.")
cityName = input("What's the name of the city your grew up in?\n")
petName = input("What's the name of your pet?\n")
bandName = cityName + " " + petName
print("Your band name could be " + bandName)

#############
### DAY 2 ###
#############

# DATA TYPES 

two_digit_number = input("Type a two digit number: ")
digitOne = two_digit_number[0]
digitTwo = two_digit_number[1]
x = int(digitOne)
y = int(digitTwo)
print(x + y)

#BMI CALCULATOR

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = float(height)
weight = int(weight)

BMI = float(weight / (height * height ))
bmiRounded = round((BMI), 2)
print(bmiRounded)

# LIFE IN WEEKS

age = input("What is your current age?\n ")

age = int(age)

totalDays = 90 * 365
totalWeeks = 90 * 52
totalMonths = 90 * 12

ageDays = age * 365
ageWeeks = age * 52
ageMonths = age * 12


daysLeft = totalDays - ageDays
weeksLeft = totalWeeks - ageWeeks
monthsLeft = totalMonths - ageMonths

print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.")

# TIP CALCULATOR

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = float(input("How much tip % would you like to give?\n"))
peopleCount = int(input("How many people are to split the bill?\n"))
billWithTip = ((tip /100) * bill) + bill
billTotal = bill + billWithTip
billPerPerson = billTotal / peopleCount
finalAmount = round(billPerPerson, 2)

print(f"Each person should pay £: {finalAmount}")

#############
### DAY 3 ###
#############

# ODD OR EVEN? INTRODUCING THE MODULO

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")

#BMI CALCULATOR 2.0

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height = float(height)
weight = int(weight)

BMI = float(weight / (height * height ))
bmiRounded = round((BMI), 2)
print(bmiRounded)

if bmiRounded < 18.5:
    print(f"Your BMI is {bmiRounded}, you are underwight.")
elif bmiRounded < 25:
    print(f"Your BMI is {bmiRounded}, you have a normal weight.")
elif bmiRounded < 30:
    print(f"Your BMI is {bmiRounded}, you are slightly overweight.")
elif bmiRounded < 35:
    print(f"Your BMI is {bmiRounded}, you are obese.")
else:
    print(f"Your BMI is {bmiRounded}, you are clinically obese.")


# LEAP YEAR

year = input("Enter a year: \n")

year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if  year % 400 == 0:
            print(f"The year {year} is a leap year.") 
        else: 
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.") 
else: 
    print(f"The year {year} is not a leap year.")

# Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0
smallPizza = 15
mediumPizza = 20
largePizza = 25
smallPepperoni = 2
medOrLargePepperoni = 3


if size == "S":
    bill += smallPizza
    if add_pepperoni == "Y":
        bill += smallPepperoni
    else: 
        bill
elif size == "M":
    bill += mediumPizza
    if add_pepperoni == "Y":
        bill += medOrLargePepperoni
elif size == "L":
    bill += largePizza
    if add_pepperoni == "Y":
        bill += medOrLargePepperoni

if extra_cheese == "Y":
    bill += 1
else: bill 

print(f"Your final bill is: ${bill}")

# LOVE CALCULATOR

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

loveNames = name1 + name2

tCount_loveNames = loveNames.count("t")
rCount_loveNames = loveNames.count("r")
uCount_loveNames = loveNames.count("u")
eCount_loveNames = loveNames.count("e")

trueCount_loveNames = tCount_loveNames + rCount_loveNames + uCount_loveNames + eCount_loveNames
trueCount_loveNames = str(trueCount_loveNames)

lCount_loveNames = loveNames.count("l")
oCount_loveNames = loveNames.count("o")
vCount_loveNames = loveNames.count("v")
eCount_loveNames = loveNames.count("e")

loveCount_loveNames = lCount_loveNames + oCount_loveNames + vCount_loveNames + eCount_loveNames
loveCount_loveNames = str(loveCount_loveNames)

loveScore = trueCount_loveNames  + loveCount_loveNames
loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90: 
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
 
# TREASURE ISLAND

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "right":
    choice2 = input('You\'ve arrived at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("'You\'ve found yourself on an island with a house. This house has 3 doors, one yellow, one blue and one red. Which one do yoou choose?\n").lower()
        if choice3 == "yellow":
            print("You entered a room full of killer bees. GAME OVER!")
        elif choice3 == "blue":     
            print("You entered  room full of toxic gas. GAME OVER!")
        elif choice3 == "red":
            print("Congratulations! You found the room with the treasure. YOU WON!")
        else: 
            print("You chose a door that doesnt exist. GAME OVER!")
    else:
        print("An angry shark attacked you. GAME OVER!")
else: 
    print("You fell into a hole. GAME OVER!")


#############
### DAY 4 ###
#############


# RANDOM MODULE

import random 

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(0, 100)
print(f"Your love score is {love_score}")


# HEADS OR TAILS

import random

random_integer = random.randint(0, 1)

if(random_integer) == 0:
    print("Heads")
else:
    print("Tails")


# UNDERSTANDING THE OFFSET AND APPENDING ITEMS TO LISTS

friends = ["Buuuju", "Joshua", "Mayowa"]

print(friends)

friends[0] = "Buju"
print(friends)

lough_friends = ["Ayo", "Adam", "Dami", "Jason"]

friends.extend(lough_friends)
print(friends)

# BANKER ROULETTE - WHO WILL PAY THE BILL?

import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
print(names)

random_integer = random.randint(0, len(names) - 1)

print(random_integer)

print(f"{names[random_integer]} is going to buy the meal today")

import random 

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
print(names)

person_who_will_pay = random.choice(names)
print(person_who_will_pay)

# TREASURE MAP

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Day 4 PROJECT: ROCK, PAPER, SCISSSORS

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")


#############
### DAY 5 ###
#############

# LOOPS

names = ["buju", "jasmine", "kronk"]

for name in names:
    print(name + " used a foor loop")


# AVERAGE HEIGHT

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
count = 0

for student in student_heights:
    total += student
    count += 1

average_height = round(total/count)
print(average_height)

# HIGHEST SCORE

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# ADDING EVEN NUMBERS

total = 0

for num in range(2, 101 ,2):
    total += num

print(total)

# FIZZBUZZ

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else: print(num)

# CREATE A PASSWORD GENERATOR 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for letter in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters

for symbol in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols

for number in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for letter in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password_list += random_letters

for symbol in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password_list+= random_symbols

for number in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password_list += random_numbers

print(password_list)

password = ""

random.shuffle(password_list)

for item in password_list:
    password += item

print(password)

#############
### DAY 7 ###
#############

# HANGMAN CHALLENGE 

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["building", "oven", "london", "table", "plant", "paper", "desktop", "coconut"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

print(display)

end_of_game = False

while end_of_game == False:

    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives])

#############
### DAY 8 ###
#############

# FUNCTIONS WITH INPUTS

def greet(name):
    print(f"Hello {name}")
    print("Hello")
    print("Hello")

greet("buju")

# POSITIONAL ARGUMENTS

def greet_with(name, location):
    print(f"My name is {name}.")
    print(f"I live in {location}.")

greet_with("Buju", "London")

# KEYWORD ARGUMENTS

def greet_with(name, location):
    print(f"My name is {name}.")
    print(f"I live in {location}.")

greet_with(location = "London", name = "Buju")

# PAINT AREA CALCULATOR

import math

def paint_calc(height, width, cover):
    area = (height * width) 
    num_of_cans = math.ceil(area/cover)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# PRIME NUMBER CHECKER

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)