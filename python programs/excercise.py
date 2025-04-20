# weight=input('enter weight in kg: ')
# height=input('enter height in meter: ')

# bmi=int(weight)/float(height) ** 2
# print(int(bmi))

# format string:
# a="bhaskar"
# b=25
# print(f"my name is {a} and i am {b} years old")

# format string
# age=int(input("enter your age: "))
# years_left=90-age
# days_left=years_left * 365
# months_left=years_left * 12
# weeks_left=years_left *52
# print(f"if you have {days_left} days, {weeks_left} weeks and {months_left} months left")

# number=int(input("enter number: "))
# if number%2==0:
#     print("this is even number")
# else:
#     print("this is odd number")


# year=int(input("which year you want to check? "))
# if year%4==0:
#     if year % 100==0:
#         if year % 400==0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")


# height=int(input("what is your age? "))
# if height>=3:
#     print("can ride")
#     age=int(input("what is your age? "))
#     if age<12:
#         bill=150
#         print("ticket price is 150")
#     elif age<=18:
#         bill=500
#         print("ticket price is 150rs")
#     else:
#         print("ticket price is 150")
#     want_photo=input("do you want to take photo(Y/N)? ")
#     if want_photo == 'y' or want_photo=='y':
#         bill =bill +50
#     print(f"your total bill is {bill}")
# else:
#     print("cant ride")
# print("bye")


# size=input("what size pizza you want(S/M/L)? ")
# bill=0
# if size =='s' or size == 's':
#     bill +=100
#     print("small pizza price is 100 rs")
# elif size =='M' or size == 'm':
#     bill+=200
#     print("medium pizza price is 200 rs")
# else:
#     bill+=300
#     print("large pizza price is 300 rs")
# add_pepperoni=input("do you want pepperoni(Y/N)?")
# if add_pepperoni == 'y' or add_pepperoni == 'y':
#     if size == 's' or size == 's':
#         bill+=30
#     else:
#         bill+=50
# extra_cheese = input("do you want pepperoni(Y/N)? ")
# if extra_cheese == 'Y' or extra_cheese == 'Y':
#     bill+=20

# print(f"your final bill is {bill}")



name1=input("what is your name?")
name2=input("what is his/her name?")
combine_string=name1+name2
lower_case_string=combine_string.lower()

t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t +r + u+e


l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l+o+v+e
love_score=int(str(true) + str(love))

if love_score < 10 or love_score >90:
    print(f"your score is {love_score} and you go to togehter like coke and mentos")

elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score} and you are alright together ")
else:
    print(f"your love score is {love_score}")
