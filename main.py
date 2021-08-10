#Data Types

#String

#print("Hello"[0])

#print("Hello"[3])

#print("Hello"[4])

#print("123" + "345")

#integer 

#print(123 + 345)

#123_456_789

#Float
# Float data type 
#3.14159

#Boolean 

#True
#False 

#a = len("clifford")
#b = len("1234")
#b = len(1234)
#print(b)

#num_char = len(input("What is your name\n"))

# Typecasting/type conversion
#This string function converts num_char into string and stores it into "new_num_char"


#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters")

# Type check
#print(type(num_char))


#a = 123
#print(type(a))

#a = str(123)
#print(type(a))

#a = float(123)
#print(type(a))

#print(70 + float("100.5"))
#print(str(70)+ str(100))

#Exercise
#two_digit_number = input("Type a two digit number: ")
#print(type(two_digit_number))


#Assigning first_digit the first subscript, second_digit the second subscript
#first_digit = int(two_digit_number[0])
#second_digit = int(two_digit_number[1])

#first_digit = two_digit_number[0]
#second_digit = two_digit_number[1]
#Converting strings into integers 
#convert1 = int(first_digit)
#convert2 = int(second_digit)

#Adding two integers
#sum = convert1 + convert2
#sum = first_digit + second_digit
#print(sum)

#print(3 + 5) 

#print (8 / 2)

#print (3 * 4)

#print (2**3)

#print (3 * 3 + 3 /3 - 3)

#print (3 * (3 + 3) /3 - 3)

#Tool for healthcare professionals 
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
#print(type(height))
#print(type(weight))

#w_height = float(height)
#w_weight = float(weight)

#BMI = int(w_weight / (w_height*w_height))
#print(BMI)

#print(int(8/3))

#Round numbers, use round function

#print(round(8/3, 2))

#print(round(2.66666, 2))

#print(type(8 // 3))

#print(type(8 / 3))

#print(type(8 / 2))

#Below variable is again divided by 2
#result = 4 / 2
#result /= 2
#print(result)

#score = 0
#score += 1
#print(score)

#fstring

#In print, all datatypes have to be SAME (for instance STRING below)
#score = 0
#height = 1.8
#isWinning = True

#print("Your score is" + " " +str(score) + " " +str(height) + " " + str(isWinning))

#instead, all of these datatypes combined into a string, removes lot of manual labor

#print(f"your score is {score}, your height is {height}, you are winning is {isWinning} ")

age = input("What is your current age?")
#print(type(age))
time_left = int(age)
#print(time_left)
R_days = (90 - time_left)*365
R_weeks = (90 - time_left)*52
R_months = (90 - time_left)*12
print(f"You have {R_days} days, {R_weeks} weeks, and {R_months} months left")

