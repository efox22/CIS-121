#1.A- this doesn't work because 
#1.B- This doesn't work because number is not defined so Define it
#!.C- yes it works
#1.D yes it works
#1.E it works but its going to keep asking forever becasue there is no user_number= 5 afeter you get it

#asking how much of everything they want
milk = int(input("How many gallons milk would you like"))
eggs = int(input("how many eggs would you like"))
bacon = int(input("How much bacon would you like"))

milkr = milk* 2
eggsr = eggs*1.5
baconr= bacon * 3
tax= (milkr+eggsr+baconr)*.11

# calculating prices
print("You got gallons of ",milk,"for",float(milkr),"dollars")
print("you got",eggs,"cartons of eggs for",float(eggsr),"dollars")
print("you got",bacon,"packs of bacon for", float(baconr),"dollars")

# calculation of final price
print("Your total is $",float((milkr+eggsr+baconr+tax)))




# I remember going over this stuff but i cant remember
# pnum = int(input("enter phone number:"))

# for pnum (1,3):
#     print("(",(1,3),")")


# bro i have no idea how to find divisors
for i in range(1,61):
    while i % 48:
        if i %2==0:
            print(i)
        if i >= 15:
            print(" I genertated the number",i,"randomly")

print("this did not go well")