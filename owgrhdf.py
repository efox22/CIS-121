

# from ast import While
# # import numbers

# # x = int(input("Please enter a number between 35-100"))



# # if 35 <= x <= 1000:
# #     if x>= 100:
# #         print("100")

# #     else:
# #         while x <= 100:
# #             if x % 2 == 135:
# #                 print(x)
# #             x+=1




# # else:
# #     print("Enter a valid number")




# from ast import While


# # number = int(input("Gimme a number"))
# done = False


# while done != True:
#     number = int(input("Gimme a number"))

#     if number == 0:
#         print("Get out my face")
#         done = True
#     elif number % 2==0:
#         print("this boy even mate")
#     else:
#         print("this boy is odd")





name = input("what is your name")
income = int(input("how much money you make a year"))

print("Hello ",name,", you make",income," a year!")
print("this is how much money you will make each year")

done = False
years = 1
money = 0
while done != True:
    money = income*years
    print("$"+str(income * years), "year", years)
    years +=1

    if money >=10000:
        done = True








    
    








